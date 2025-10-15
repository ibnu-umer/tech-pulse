import aiohttp

BASE_URL = "https://www.reddit.com/search.json"


async def fetch_reddit(session, topic, limit):
    """Fetch top Reddit posts related to a topic."""
    params = {
        "q": topic,
        "sort": "hot",
        "limit": limit,
        "t": "week"  # restrict to recent content
    }

    headers = {
        "User-Agent": "TechPulseBot/1.0"  # Reddit requires a user agent
    }

    try:
        async with session.get(BASE_URL, headers=headers, params=params, timeout=10) as resp:
            if resp.status != 200:
                text = await resp.text()
                return [{
                    "source": "reddit",
                    "topic": topic,
                    "error": f"HTTP {resp.status}: {text[:100]}",
                }]

            data = await resp.json()
            posts = data.get("data", {}).get("children", [])
            results = []

            for post in posts:
                p = post.get("data", {})
                results.append({
                    "title": p.get("title"),
                    "url": f"https://www.reddit.com{p.get('permalink')}",
                    "description": p.get("selftext") or "No description available.",
                    "popularity": p.get("ups", 0),
                })

            return {
                "source": "reddit",
                "topic": topic,
                "results": results
            }

    except Exception as e:
        return [{
            "source": "reddit",
            "topic": topic,
            "error": str(e)
        }]
