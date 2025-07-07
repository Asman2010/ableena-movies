import asyncio
from crawl4ai import AsyncWebCrawler
import pyperclip


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://www.1tamilmv.onl",
        )
        print(result.html)
        pyperclip.copy(result.media)


if __name__ == "__main__":
    asyncio.run(main())
