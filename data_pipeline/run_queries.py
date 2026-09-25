import sqlite3
import pandas as pd

DB_FILE = "data_pipeline/zepto_books.db"
OUTPUT_FILE = "data_pipeline/query_results.md"

queries = [
    (
        "Query 1 — WHERE",
        """
        SELECT title, price_gbp
        FROM books
        WHERE price_gbp > 30;
        """
    ),
    (
        "Query 2 — ORDER BY and LIMIT",
        """
        SELECT title, price_gbp
        FROM books
        ORDER BY price_gbp DESC
        LIMIT 10;
        """
    ),
    (
        "Query 3 — DISTINCT",
        """
        SELECT DISTINCT star_rating
        FROM books
        ORDER BY star_rating;
        """
    ),
    (
        "Query 4 — BETWEEN",
        """
        SELECT title, price_gbp, star_rating
        FROM books
        WHERE price_gbp BETWEEN 10 AND 20;
        """
    ),
    (
        "Query 5 — IN",
        """
        SELECT title, price_gbp, price_inr
        FROM books
        WHERE star_rating IN (4, 5);
        """
    ),
    (
        "Query 6 — JOIN",
        """
        SELECT
            books.title,
            books.price_gbp,
            books.price_inr,
            books.star_rating,
            categories.category_name
        FROM books
        JOIN categories
        ON books.category_id = categories.category_id
        ORDER BY books.price_inr DESC
        LIMIT 10;
        """
    )
]

connection = sqlite3.connect(DB_FILE)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("# SQL Query Results\n\n")

    for name, query in queries:
        df = pd.read_sql(query, connection)

        file.write(f"## {name}\n\n")
        file.write("```sql\n")
        file.write(query.strip())
        file.write("\n```\n\n")
        file.write("### Output\n\n")
        file.write(df.to_markdown(index=False))
        file.write("\n\n")

    books_df = pd.read_sql("""
        SELECT
            title,
            price_gbp,
            price_inr,
            star_rating,
            category_id
        FROM books
    """, connection)

    categories_df = pd.read_sql("""
        SELECT
            category_id,
            category_name
        FROM categories
    """, connection)

    merge_df = pd.merge(
        books_df,
        categories_df,
        on="category_id",
        how="inner"
    )

    merge_df = merge_df[
        ["title", "price_gbp", "price_inr", "star_rating", "category_name"]
    ]

    merge_df = merge_df.sort_values(
        "price_inr",
        ascending=False
    ).head(10)

    file.write("## pandas.merge Result\n\n")
    file.write(merge_df.to_markdown(index=False))
    file.write("\n")

connection.close()

print("All SQL queries executed successfully.")
print("Query results saved to:", OUTPUT_FILE)
print("Pandas merge completed successfully.")