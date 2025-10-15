import aiohttp
import asyncio
from apis.news_api import fetch_news
from apis.reddit_api import fetch_reddit
from apis.github_api import fetch_github
import logging

logger = logging.getLogger(__name__)

async def fetch_all(topics, limit=None):
    logger.info(f"Fetching data for {topics}")
    async with aiohttp.ClientSession() as session:
        tasks = []
        for topic in topics:
            tasks += [
                fetch_news(session, topic, limit),
                fetch_github(session, topic, limit),
                fetch_reddit(session, topic, limit)
            ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        logger.info("Data fetched for topics.")
        return results
