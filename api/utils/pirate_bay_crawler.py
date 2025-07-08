import sys
from pathlib import Path
from typing import Dict
from urllib.parse import urlencode

# Add the parent directory to the path so we can import from utils
sys.path.append(str(Path(__file__).parent.parent))


from utils.crawl import crawler


def build_piratebay_url(query: str, category: int = 0) -> str:
    """
    Build The Pirate Bay search URL.

    Args:
        query: Search query
        category: Category ID (0 for all categories)

    Returns:
        Complete search URL
    """
    base_url = "https://thepiratebay.org/search.php"
    params = {"q": query, "cat": category}
    return f"{base_url}?{urlencode(params)}"


async def scrape_piratebay(query: str, category: int = 0) -> Dict:
    """
    Scrape The Pirate Bay search results.

    Args:
        query: Search query
        category: Category ID (0 for all categories)

    Returns:
        Dictionary containing scraped data
    """
    # Build search URL
    search_url = build_piratebay_url(query, category)

    links_data = await crawler(search_url)

    return links_data["internal"]
