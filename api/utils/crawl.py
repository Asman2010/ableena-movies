import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, GeolocationConfig
import pyperclip
import json
from typing import Dict

from .search import search

LOCATIONS = [
    {"latitude": 40.7128, "longitude": -74.0060, "name": "New York, USA", "timezone": "America/New_York", "locale": "en-US"},
    {"latitude": 51.5074, "longitude": -0.1278, "name": "London, UK", "timezone": "Europe/London", "locale": "en-GB"},
    {"latitude": 43.6532, "longitude": -79.3832, "name": "Toronto, Canada", "timezone": "America/Toronto", "locale": "en-CA"},
    {"latitude": -33.8688, "longitude": 151.2093, "name": "Sydney, Australia", "timezone": "Australia/Sydney", "locale": "en-AU"},
    {"latitude": 1.3521, "longitude": 103.8198, "name": "Singapore", "timezone": "Asia/Singapore", "locale": "en-SG"}
]

async def crawler(url: str, max_retries: int = 5) -> Dict:
    """
    Crawl website with location fallback mechanism.
    
    Args:
        url: URL to crawl
        max_retries: Maximum number of location retries
        
    Returns:
        Crawled links data or None if all locations fail
    """
    
    for attempt in range(min(max_retries, len(LOCATIONS))):
        location = LOCATIONS[attempt]
        
        try:
            print(f"Attempt {attempt + 1}: Trying location {location['name']}")
            
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
                
                if result and hasattr(result, 'links') and result.links:
                    internal_links = result.links.get('internal', [])
                    if internal_links:
                        print(f"✅ Success with {location['name']} - Found {len(internal_links)} internal links")
                        return result.links
                    else:
                        print(f"❌ No internal links found with {location['name']}")
                else:
                    print(f"❌ No valid result from {location['name']}")
                    
        except Exception as e:
            print(f"❌ Error with {location['name']}: {str(e)}")
            continue
    
    print("❌ All locations failed!")
    return None

# async def main():
#     """
#     Main function that crawls with fallback and demonstrates search.
#     """
#     url = "https://www.1tamilmv.onl"
    
#     # Crawl with location fallback
#     links_data = await crawler(url)
#     pyperclip.copy(json.dumps(links_data, indent=2))
    
#     if not links_data:
#         print("Failed to crawl the website with all locations")
#         return
    
#     # Combined search
#     results = search(links_data, search_term="ballerina")
#     print(results)

#     return results

# if __name__ == "__main__":
#     asyncio.run(main())
