from flask import Flask, render_template, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    try:
        url = "https://feeds.bbci.co.uk/news/rss.xml"
        response = requests.get(url, timeout=10)
        
        from xml.etree import ElementTree
        root = ElementTree.fromstring(response.content)
        items = root.findall(".//item")
        
        news_data = []
        for item in items[:5]:
            title = item.find("title").text if item.find("title") is not None else "No title"
            link = item.find("link").text if item.find("link") is not None else "#"
            pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""
            news_data.append({
                "title": title,
                "link": link,
                "source": "BBC",
                "published": pub_date
            })
        
        return jsonify({"status": "success", "data": news_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/crypto')
def get_crypto():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 5,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=params, timeout=10)
        coins = response.json()
        
        crypto_data = []
        for coin in coins:
            crypto_data.append({
                "name": coin.get("name", "Unknown"),
                "symbol": coin.get("symbol", "?").upper(),
                "price": coin.get("current_price", 0),
                "change_24h": coin.get("price_change_percentage_24h", 0)
            })
        
        return jsonify({"status": "success", "data": crypto_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/api/products')
def get_products():
    try:
        url = "https://fakestoreapi.com/products"
        response = requests.get(url, timeout=10)
        products = response.json()[:5]
        
        product_data = []
        for p in products:
            product_data.append({
                "title": p.get("title", "No title"),
                "price": p.get("price", 0),
                "url": f"https://fakestoreapi.com/products/{p.get('id', 1)}"
            })
        
        return jsonify({"status": "success", "data": product_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)