# Universal Scraper Dashboard

A Flask-based web scraper that collects data from multiple sources with a modern Tailwind CSS interface.

## Features

- **News Scraping**: BBC RSS feed headlines
- **Crypto Data**: Real-time cryptocurrency prices from CoinGecko
- **Product Data**: Sample products from FakeStore API
- **Modern UI**: Dark theme dashboard with Tailwind CSS

## Quick Start

```bash
cd universal_scraper
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## API Endpoints

- `GET /` - Dashboard interface
- `GET /scrape/all` - Run all scrapers
- `GET /data/news` - Get news data
- `GET /data/crypto` - Get crypto data  
- `GET /data/products` - Get product data

## Data Sources

- **News**: BBC RSS (https://feeds.bbci.co.uk/news/rss.xml)
- **Crypto**: CoinGecko API
- **Products**: FakeStore API (https://fakestoreapi.com)

## File Structure

```
universal_scraper/
├── app.py              # Flask routes
├── scraper.py          # Scraping functions
├── requirements.txt    # Dependencies
├── templates/
│   └── index.html      # Dashboard UI
└── data/
    ├── news.csv
    ├── crypto.csv
    └── products.csv
```