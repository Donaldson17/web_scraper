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
    return jsonify({"status": "All scrapers ran successfully."})

@app.route("/data/news")
def get_news_data():
    path = "data/news.csv"
    return jsonify(read_csv(path))

@app.route("/data/crypto")
def get_crypto_data():
    path = "data/crypto.csv"
    return jsonify(read_csv(path))

@app.route("/data/products")
def get_product_data():
    path = "data/products.csv"
    return jsonify(read_csv(path))

def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

if __name__ == "__main__":
    app.run(debug=True)
