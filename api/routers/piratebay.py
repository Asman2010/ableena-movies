from fastapi import APIRouter, Query
from utils.crawl import crawler
from utils.magnet_links_fetcher import get_magnet_links
from urllib.parse import urlencode

router = APIRouter(
    prefix="/piratebay",
    tags=["piratebay"],
)

# Base URL for TamilMV
PIRATEBAY_BASE_URL = "https://thepiratebay.org/search.php"


def build_piratebay_url(query: str, category: int = 0) -> str:
    """1
    Build The Pirate Bay search URL.

    Args:
        query: Search query
        category: Category ID (0 for all categories)

    Returns:
        Complete search URL
    """
    base_url = PIRATEBAY_BASE_URL
    params = {"q": query, "cat": category}
    return f"{base_url}?{urlencode(params)}"


@router.get("/search/")
async def search_piratebay_endpoint(
    query: str = Query(..., description="Search query"),
    category: int = Query(0, description="Category ID"),
):
    """
    Search Piratebay for the given query and return matching topics.

    - **query**: The search term to look for the movie
    """
    urls = build_piratebay_url(query, category)
    results = await crawler(urls)

    return results["internal"]


@router.get("/magnet_fetcher/")
async def get_magnet_links_endpoint(
    url: str = Query(..., description="URL to scrape for magnet links"),
):
    """
    Scrape a URL and extract all magnet links.

    - **url**: The URL to scrape for magnet links
    """
    magnet_links = await get_magnet_links(url)
    return magnet_links
