from fastapi import APIRouter, Query
from utils.crawl import crawler
from utils.search import search
from utils.magnet_links_fetcher import get_magnet_links

router = APIRouter(
    prefix="/tamilmv",
    tags=["tamilmv"],
    responses={404: {"description": "Not found"}},
)

# Base URL for TamilMV
TAMILMV_BASE_URL = "https://www.1tamilmv.onl"


@router.get("/search/")
async def search_tamilmv_endpoint(
    query: str = Query(..., description="Search query"),
):
    """
    Search TamilMV for the given query and return matching topics.

    - **query**: The search term to look for
    """

    urls = await crawler(TAMILMV_BASE_URL)
    results = search(urls, search_term=query)

    if not results:
        TAMILMV_SEARCH_URL = f"{TAMILMV_BASE_URL}/index.php?/search/&q={query}&quick=1&search_and_or=or&sortby=relevancy"
        raw_results = await crawler(TAMILMV_SEARCH_URL)
        results = raw_results["internal"]

    return results


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
