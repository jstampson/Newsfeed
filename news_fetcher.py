import feedparser

RSS_FEEDS = {
    "VentureBeat": "https://venturebeat.com/category/ai/feed/",
    "Google" : "https://research.google/blog/rss/",
    "Berkeley" : "https://bair.berkeley.edu/blog/feed.xml",
    "MIT" : "https://news.mit.edu/rss/topic/artificial-intelligence2"
    }

    
def fetch_news(max_items_per_feed=2):

    """
    Fetches news items from RSS feeds.

    Args:
        max_items_per_feed (int): Maximum number of items to fetch from each feed.

    Returns:
        list: List of news items, each represented as a dictionary with keys
            "source", "title", "summary", and "link".
    """

    news_items = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        entries = feed.entries[:max_items_per_feed]  # Limit per feed

        for entry in entries:
            news_items.append({
                "source": source,
                "title": entry.title,
                "summary": entry.get("summary", "").strip(),
                "link": entry.link
            })

    return news_items




if __name__ == "__main__":
    news = fetch_news()
    for item in news:
        print(f"[{item['source']}] {item['title']}")
        print(item['summary'])
        print(item['link'])
        print("-" * 60)