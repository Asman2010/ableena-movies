from typing import Dict, Optional, List
from urllib.parse import unquote, parse_qs
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, GeolocationConfig
import re
from .crawl import LOCATIONS

def parse_magnet_link(magnet_url: str) -> Dict:
    """
    Parse magnet link and extract useful information.
    
    Args:
        magnet_url: Raw magnet link
        
    Returns:
        Dictionary with parsed magnet link info
    """
    try:
        # Remove magnet: prefix if present
        if magnet_url.startswith('magnet:'):
            magnet_url = magnet_url[7:]
        
        # Parse the query string
        if magnet_url.startswith('?'):
            magnet_url = magnet_url[1:]
        
        params = parse_qs(magnet_url)
        
        # Extract common magnet parameters
        magnet_info = {
            'magnet_link': f"magnet:?{magnet_url}",
            'display_name': None,
            'info_hash': None,
            'trackers': [],
            'file_size': None,
            'exact_topic': None
        }
        
        # Extract display name (dn parameter)
        if 'dn' in params:
            magnet_info['display_name'] = unquote(params['dn'][0])
        
        # Extract info hash (xt parameter)
        if 'xt' in params:
            xt = params['xt'][0]
            if xt.startswith('urn:btih:'):
                magnet_info['info_hash'] = xt[9:]
        
        # Extract trackers (tr parameters)
        if 'tr' in params:
            magnet_info['trackers'] = [unquote(tracker) for tracker in params['tr']]
        
        # Extract file size if available (xl parameter)
        if 'xl' in params:
            try:
                magnet_info['file_size'] = int(params['xl'][0])
            except ValueError:
                pass
        
        # Extract exact topic if available (kt parameter)
        if 'kt' in params:
            magnet_info['exact_topic'] = unquote(params['kt'][0])
        
        return magnet_info
        
    except Exception as e:
        return {
            'magnet_link': magnet_url if magnet_url.startswith('magnet:') else f"magnet:?{magnet_url}",
            'display_name': None,
            'info_hash': None,
            'trackers': [],
            'file_size': None,
            'exact_topic': None,
            'parse_error': str(e)
        }

def format_file_size(size_bytes: Optional[int]) -> str:
    """
    Format file size in human readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string
    """
    if size_bytes is None:
        return "Unknown"
    
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} PB"

async def get_magnet_links(url: str, max_retries: int = 5) -> List[Dict]:
    """
    Scrape a URL and extract all magnet links.
    
    Args:
        url: URL to scrape for magnet links
        max_retries: Maximum number of location retries
        
    Returns:
        List of dictionaries containing magnet link information
    """
    
    # Try different locations until we get results
    for attempt in range(min(max_retries, len(LOCATIONS))):
        location = LOCATIONS[attempt]
        
        try:
            print(f"Attempt {attempt + 1}: Scraping with {location['name']}")
            
            async with AsyncWebCrawler() as crawler:
                crun_cfg = CrawlerRunConfig(
                    url=url,
                    locale=location["locale"],
                    timezone_id=location["timezone"],
                    geolocation=GeolocationConfig(
                        latitude=location["latitude"],
                        longitude=location["longitude"],
                        accuracy=10.0,
                    )
                )
                
                result = await crawler.arun(url, run_cfg=crun_cfg)
                
                if result and hasattr(result, 'markdown') and result.markdown:
                    # Extract magnet links from the page content
                    magnet_pattern = r'magnet:\?[^\s<>"\']*'
                    magnet_matches = re.findall(magnet_pattern, result.markdown, re.IGNORECASE)
                    
                    if magnet_matches:
                        print(f"✅ Found {len(magnet_matches)} magnet links with {location['name']}")
                        
                        # Parse each magnet link
                        magnet_links = []
                        for magnet_url in magnet_matches:
                            # Clean up the magnet URL (remove trailing punctuation)
                            magnet_url = re.sub(r'[.,;!?]+$', '', magnet_url)
                            
                            parsed_magnet = parse_magnet_link(magnet_url)
                            
                            # Add formatted file size
                            if parsed_magnet['file_size']:
                                parsed_magnet['file_size_formatted'] = format_file_size(parsed_magnet['file_size'])
                            else:
                                parsed_magnet['file_size_formatted'] = "Unknown"
                            
                            magnet_links.append(parsed_magnet)
                        
                        # Remove duplicates based on info_hash
                        unique_magnets = []
                        seen_hashes = set()
                        
                        for magnet in magnet_links:
                            hash_key = magnet['info_hash'] or magnet['magnet_link']
                            if hash_key not in seen_hashes:
                                unique_magnets.append(magnet)
                                seen_hashes.add(hash_key)
                        
                        return unique_magnets
                    else:
                        print(f"❌ No magnet links found with {location['name']}")
                else:
                    print(f"❌ No valid content from {location['name']}")
                    
        except Exception as e:
            print(f"❌ Error with {location['name']}: {str(e)}")
            continue
    
    print("❌ All locations failed to find magnet links!")
    return []

# Example usage function
# async def demo_magnet_scraper():
#     """
#     Demo function showing how to use the magnet scraper.
#     """
#     # Example URL (replace with actual URL from your search results)
#     test_url = "https://thepiratebay.org/search.php?q=thug+life&all=on&search=Pirate+Search&page=0&orderby="
    
#     print(f"Scraping magnet links from: {test_url}")
    
#     magnet_links = await get_magnet_links(test_url)
    
#     if magnet_links:
#         print(f"\n=== FOUND {len(magnet_links)} MAGNET LINKS ===")
        
#         for i, magnet in enumerate(magnet_links, 1):
#             print(f"\n{i}. {magnet['display_name'] or 'Unknown Name'}")
#             print(f"   Size: {magnet['file_size_formatted']}")
#             print(f"   Hash: {magnet['info_hash'] or 'Unknown'}")
#             print(f"   Trackers: {len(magnet['trackers'])} trackers")
#             print(f"   Magnet: {magnet['magnet_link'][:80]}...")
            
#             if magnet.get('parse_error'):
#                 print(f"   ⚠️  Parse Error: {magnet['parse_error']}")
#     else:
#         print("No magnet links found!")
    
#     return magnet_links

# if __name__ == "__main__":
#     # Run the demo
#     asyncio.run(demo_magnet_scraper())