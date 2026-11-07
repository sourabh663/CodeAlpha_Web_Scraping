"""
Task 1: Web Scraping
Scrapes book information from https://books.toscrape.com/
Run: python scraping.py
Output: output/books_dataset.csv

This is a practice website intended for learning web scraping.
The script follows pagination and uses a short delay between requests.
"""
import time
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup

START_URL = "https://books.toscrape.com/"
OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "books_dataset.csv"
HEADERS = {
    "User-Agent": "EducationalWebScraper/1.0 (learning project)"
}
RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}


def scrape_books():
    """Collect book details from every catalogue page."""
    session = requests.Session()
    session.headers.update(HEADERS)

    current_url = START_URL
    records = []

    while current_url:
        print(f"Scraping: {current_url}")
        response = session.get(current_url, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title_link = book.select_one("h3 a")
            price_element = book.select_one(".price_color")
            rating_element = book.select_one("p.star-rating")
            availability_element = book.select_one(
                ".instock.availability"
            )

            if not title_link or not price_element:
                continue

            rating_word = ""
            rating_value = None
            if rating_element:
                classes = rating_element.get("class", [])
                rating_word = next(
                    (item for item in classes if item in RATING_MAP), ""
                )
                rating_value = RATING_MAP.get(rating_word)

            records.append({
                "title": title_link.get("title", "").strip(),
                "price": price_element.get_text(strip=True),
                "rating": rating_word,
                "rating_numeric": rating_value,
                "availability": (
                    availability_element.get_text(" ", strip=True)
                    if availability_element else "Unknown"
                ),
                "product_url": urljoin(current_url, title_link.get("href", ""))
            })

        next_link = soup.select_one("li.next a")
        current_url = (
            urljoin(current_url, next_link.get("href"))
            if next_link else None
        )

        # Be considerate to the practice website.
        if current_url:
            time.sleep(1)

    return records


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    records = scrape_books()

    if not records:
        print("No books were found. Please check the website connection.")
        return

    dataframe = pd.DataFrame(records)
    dataframe.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"\nFinished! Collected {len(dataframe)} books.")
    print(f"CSV saved to: {OUTPUT_FILE.resolve()}")
    print("\nPreview:")
    print(dataframe.head(10).to_string(index=False))


if __name__ == "__main__":
    main()
