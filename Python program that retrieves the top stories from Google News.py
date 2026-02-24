# Write a Python program that retrieves the top stories from Google News.

import feedparser

def get_top_google_news():
    rss_url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
    news_feed = feedparser.parse(rss_url)
    top_stories = news_feed.entries

    print("\nTop Google News Stories:\n")
    for i, story in enumerate(top_stories, start=1):
        title = story.title
        link = story.link
        print(f"{i}. {title}")
        print(f"   Link: {link}\n")
if __name__ == "__main__":
    get_top_google_news()