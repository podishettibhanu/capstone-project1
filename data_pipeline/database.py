import sqlite3
import pandas as pd

CSV_FILE = "data_pipeline/books_cleaned.csv"
DB_FILE = "data_pipeline/zepto_books.db"

def create_database():
    df = pd.read_csv(CSV_FILE)

    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price_gbp REAL,
            price_inr REAL,
            star_rating INTEGER,
            in_stock INTEGER,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    """)

    for category in df["category"].dropna().unique():
        cursor.execute(
            "INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
            (category,)
        )

    for _, row in df.iterrows():
        cursor.execute(
            "SELECT category_id FROM categories WHERE category_name = ?",
            (row["category"],)
        )

        category_id = cursor.fetchone()[0]

        cursor.execute("""
            INSERT INTO books (
                title,
                price_gbp,
                price_inr,
                star_rating,
                in_stock,
                category_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row["title"],
            row["price_gbp"],
            row["price_inr"],
            row["star_rating"],
            int(row["in_stock"]),
            category_id
        ))

    connection.commit()

    print("Database created successfully.")
    print("Books inserted:", len(df))

    cursor.execute("SELECT COUNT(*) FROM categories")
    print("Categories inserted:", cursor.fetchone()[0])

    connection.close()

if __name__ == "__main__":
    create_database()