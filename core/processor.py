from collections import defaultdict
from datetime import datetime, timezone




def process_data(raw_data):
    """
    Takes the raw list of API responses and groups them by topic.
    Returns a dict of topic -> list of cleaned items.
    """
    if not raw_data:
        print("[processor] No data received.")
        return {}

    grouped = defaultdict(list)

    for topic_data in raw_data:
        source = topic_data.get("source", "unknown")
        results = topic_data.get("results", [])

        for result in results:
            popularity = result.get("popularity", None)
            topic = topic_data.get("topic", "unknown")

            if popularity is None:
                if source == "news":
                    # Infer by recency (newer = more popular)
                    published = result.get("publishedAt")
                    popularity = _score_by_recency(published)
                elif source == "reddit":
                    # Combine upvotes + comments
                    ups = result.get("ups", 0)
                    comments = result.get("num_comments", 0)
                    popularity = ups + (comments * 2)
                elif source == "github":
                    stars = result.get("stargazers_count", 0)
                    forks = result.get("forks_count", 0)
                    popularity = stars + (forks * 3)
                else:
                    popularity = 0  # default fallback


            grouped[topic].append({
                "source": result.get("source", "unknown"),
                "title": result.get("title", "").strip(),
                "description": result.get("description", "").strip(),
                "popularity": popularity
            })

    # Sort each topic's items by popularity descending
    for topic in grouped:
        grouped[topic] = sorted(grouped[topic], key=lambda x: x["popularity"], reverse=True)

    print(f"[processor] Processed data for {len(grouped)} topics.")
    return dict(grouped)



def _score_by_recency(published_at):
    """
    Converts a date string into a recency-based popularity score (0-100).
    """
    if not published_at:
        return 0

    try:
        published_time = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        age_hours = (datetime.now(timezone.utc) - published_time).total_seconds() / 3600
        score = max(0, 100 - age_hours)  # newer = higher score
        return round(score, 2)
    except Exception:
        return 0
