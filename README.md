# Task 1 — Web Scraping Project

## Project overview
This beginner-friendly project extracts book titles, prices, star ratings, availability, and product-page links from the public practice website **Books to Scrape**.

Website: https://books.toscrape.com/

## What is included?
- `scraping.py` — Python scraper that visits catalogue pages and follows pagination.
- `requirements.txt` — Python packages needed.
- `output/books_dataset.csv` — small illustrative preview dataset. Run the scraper to replace it with freshly collected website data.
- `project_report.docx` — project documentation and methodology.
- `screenshots/` — place your own screenshots here after running the program.

## How to run (Windows / macOS / Linux)

1. Install Python 3.9 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the scraper:

   ```bash
   python scraping.py
   ```

5. The complete dataset will be saved as `output/books_dataset.csv`.

If your computer uses `python3`, run `python3 -m pip install -r requirements.txt` and `python3 scraping.py`.

## Dataset fields
| Column | Meaning |
|---|---|
| title | Book title |
| price | Displayed book price |
| rating | Star rating as words |
| rating_numeric | Star rating from 1 to 5 |
| availability | Availability text shown on the page |
| product_url | Link to the individual book page |

## Important note
The CSV included before running the script is an **illustrative preview**, not a claim of a fresh live scrape. The Python program performs the live scrape when you run it. Use the website only for learning, respect its terms and access rules, and do not use scraping to collect private or restricted information.
