import requests
import csv
from datetime import datetime
import os

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

# ------------------------------
# 📰 NEWS SCRAPER (BBC RSS)
# ------------------------------
def scrape_news():
    try:
        print("Scraping BBC News...")
        url = "https://feeds.bbci.co.uk/news/rss.xml"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        
        from xml.etree import ElementTree
        root = ElementTree.fromstring(res.content)
        items = root.findall(".//item")

        data = []
        for item in items[:10]:  # first 10 items
            title = item.find("title").text if item.find("title") is not None else "No title"
            link = item.find("link").text if item.find("link") is not None else "#"
            pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""
            data.append({
                "published": pub_date,
                "title": title,
                "link": link,
                "source": "BBC"
            })

        save_csv("data/news.csv", data, ["published", "title", "link", "source"])
        print("News data saved.")
        return True
    except Exception as e:
        print(f"News scraping failed: {e}")
        return False


# ------------------------------
# 💰 CRYPTO SCRAPER (CoinGecko API)
# ------------------------------
def scrape_crypto():
    try:
        print("Scraping Crypto Data...")
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 5,
            "page": 1,
            "sparkline": False
        }
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        coins = res.json()

        data = []
        for coin in coins:
            data.append({
                "name": coin.get("name", "Unknown"),
                "symbol": coin.get("symbol", "?").upper(),
                "price": coin.get("current_price", 0),
                "market_cap": coin.get("market_cap", 0),
                "change_24h": coin.get("price_change_percentage_24h", 0)
            })

        save_csv("data/crypto.csv", data, ["name", "symbol", "price", "market_cap", "change_24h"])
        print("Crypto data saved.")
        return True
    except Exception as e:
        print(f"Crypto scraping failed: {e}")
        return False


# ------------------------------
# 🛍️ PRODUCT SCRAPER (Example from Fake Store API)
# ------------------------------
def scrape_products():
    try:
        print("Scraping Product Data...")
        url = "https://fakestoreapi.com/products"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        products = res.json()[:8]  # first 8 products

        data = []
        for p in products:
            data.append({
                "title": p.get("title", "No title"),
                "price": p.get("price", 0),
                "url": f"https://fakestoreapi.com/products/{p.get('id', 1)}"
            })

        save_csv("data/products.csv", data, ["title", "price", "url"])
        print("Product data saved.")
        return True
    except Exception as e:
        print(f"Product scraping failed: {e}")
        return False


# ------------------------------
# 💾 CSV Writer
# ------------------------------
def save_csv(path, data, headers):
    try:
        with open(path, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Failed to save {path}: {e}")


# ------------------------------
# 🧩 Run all manually for test
# ------------------------------
if __name__ == "__main__":
    scrape_news()
    scrape_crypto()
    scrape_products()
    print("All scraping complete!")
