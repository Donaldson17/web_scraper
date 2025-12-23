from flask import Flask, render_template, jsonify
import csv, json, os
from scraper import scrape_news, scrape_crypto, scrape_products

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape/all")
def scrape_all():
    scrape_news()
    scrape_crypto()
    scrape_products()
    return jsonify({"status": "success", "message": "All scrapers completed"})

@app.route("/scrape/news")
def scrape_news_endpoint():
    try:
        success = scrape_news()
        if success:
            return jsonify({"status": "success", "data": read_csv("data/news.csv")})
        else:
            return jsonify({"status": "error", "message": "Failed to scrape news"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/scrape/crypto")
def scrape_crypto_endpoint():
    try:
        success = scrape_crypto()
        if success:
            return jsonify({"status": "success", "data": read_csv("data/crypto.csv")})
        else:
            return jsonify({"status": "error", "message": "Failed to scrape crypto"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/scrape/products")
def scrape_products_endpoint():
    try:
        success = scrape_products()
        if success:
            return jsonify({"status": "success", "data": read_csv("data/products.csv")})
        else:
            return jsonify({"status": "error", "message": "Failed to scrape products"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route("/data/news")
def get_news_data():
    return jsonify(read_csv("data/news.csv"))

@app.route("/data/crypto")
def get_crypto_data():
    return jsonify(read_csv("data/crypto.csv"))

@app.route("/data/products")
def get_product_data():
    return jsonify(read_csv("data/products.csv"))

def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

if __name__ == "__main__":
    app.run(debug=True)
