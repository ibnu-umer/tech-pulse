import aiohttp
import asyncio
from apis.news_api import fetch_news
from apis.reddit_api import fetch_reddit
from apis.github_api import fetch_github



async def fetch_all(topics, limit=None):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for topic in topics:
            tasks += [
                fetch_news(session, topic, limit),
            ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
