import os


BASE_URL = "https://api.github.com/search/repositories"


async def fetch_github(session, topic, limit):
    """Fetch trending GitHub repos related to a topic."""
    params = {
        "q": f"{topic} in:name,description,topics",
        "sort": "stars",
        "order": "desc",
        "per_page": limit,
    }

    headers = {
        "Accept": "application/vnd.github+json",
    }

    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        async with session.get(BASE_URL, headers=headers, params=params, timeout=10) as resp:
            if resp.status != 200:
                text = await resp.text()
                return {
                    "source": "github",
                    "topic": topic,
                    "error": f"HTTP {resp.status}: {text[:100]}",
                }

            data = await resp.json()
            results = []

            for repo in data.get("items", []):
                results.append({
                    "title": repo["name"],
                    "url": repo["html_url"],
                    "description": repo.get("description") or "No description available.",
                    "popularity": repo.get("stargazers_count", 0)
                })

            return {
                "source": "github",
                "topic": topic,
                "results": results
            }

    except Exception as e:
        return {
            "source": "github",
            "topic": topic,
            "error": str(e)
        }
