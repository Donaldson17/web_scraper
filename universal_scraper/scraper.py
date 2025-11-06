import requests
import csv
from datetime import datetime

# ------------------------------
# 📰 NEWS SCRAPER (BBC RSS)
# ------------------------------
def scrape_news():
    print("Scraping BBC News...")
    url = "https://feeds.bbci.co.uk/news/rss.xml"
    res = requests.get(url)
    from xml.etree import ElementTree

    root = ElementTree.fromstring(res.content)
    items = root.findall(".//item")

    data = []
    for item in items[:10]:  # first 10 items
        title = item.find("title").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""
        data.append({
            "published": pub_date,
            "title": title,
            "link": link,
            "source": "BBC"
        })

    save_csv("data/news.csv", data, ["published", "title", "link", "source"])
    print("✅ News data saved.")


# ------------------------------
# 💰 CRYPTO SCRAPER (CoinGecko API)
# ------------------------------
def scrape_crypto():
    print("Scraping Crypto Data...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": False
    }
    res = requests.get(url, params=params)
    coins = res.json()

    data = []
    for coin in coins:
        data.append({
            "name": coin["name"],
            "symbol": coin["symbol"].upper(),
            "price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "change_24h": coin["price_change_percentage_24h"]
        })

    save_csv("data/crypto.csv", data, ["name", "symbol", "price", "market_cap", "change_24h"])
    print("✅ Crypto data saved.")


# ------------------------------
# 🛍️ PRODUCT SCRAPER (Example from Fake Store API)
# ------------------------------
def scrape_products():
    print("Scraping Product Data...")
    url = "https://fakestoreapi.com/products"
    res = requests.get(url)
    products = res.json()[:8]  # first 8 products

    data = []
    for p in products:
        data.append({
            "title": p["title"],
            "price": p["price"],
            "url": f"https://fakestoreapi.com/products/{p['id']}"
        })

    save_csv("data/products.csv", data, ["title", "price", "url"])
    print("✅ Product data saved.")


# ------------------------------
# 💾 CSV Writer
# ------------------------------
def save_csv(path, data, headers):
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


# ------------------------------
# 🧩 Run all manually for test
# ------------------------------
if __name__ == "__main__":
    scrape_news()
    scrape_crypto()
    scrape_products()
    print("✅ All scraping complete!")
