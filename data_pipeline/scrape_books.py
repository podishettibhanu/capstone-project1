import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books():
    books = []

    for page in range(1, 6):
        url = BASE_URL.format(page)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]

            price_text = book.select_one(".price_color").get_text(strip=True)

            rating_text = book.select_one("p.star-rating")["class"][1]

            availability_text = book.select_one(
                ".availability"
            ).get_text(" ", strip=True)

            book_url = urljoin(url, book.h3.a["href"])

            book_response = requests.get(book_url, timeout=10)
            book_response.raise_for_status()

            book_soup = BeautifulSoup(book_response.text, "html.parser")

            category_link = book_soup.select_one(
                "ul.breadcrumb li:nth-child(3) a"
            )

            category = (
                category_link.get_text(strip=True)
                if category_link
                else "Unknown"
            )

            books.append({
                "title": title,
                "price_gbp": price_text,
                "star_rating": rating_text,
                "availability": availability_text,
                "category": category
            })

    return pd.DataFrame(books)

if __name__ == "__main__":
    df = scrape_books()

    df.to_csv("data_pipeline/books_raw.csv", index=False)

    print("Number of books:", len(df))
    print(df.head())
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nNumber of categories:")
    print(df["category"].nunique())
    print("\nCategories:")
    print(df["category"].value_counts())
    print("\nRaw data saved successfully.")
    