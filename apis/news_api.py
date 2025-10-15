import os, aiohttp

BASE_URL = "https://gnews.io/api/v4/search"

async def fetch_news(session, topic, limit):
    api_key = os.getenv("NEWS_API_KEY")
    params = {"q": topic, "lang": "en", "token": api_key, "max": limit}
    async with session.get(BASE_URL, params=params) as resp:
        data = await resp.json()
        return {"source": "news", "topic": topic, "results": data.get("articles", []), "errors": data.get("errors", [])}
