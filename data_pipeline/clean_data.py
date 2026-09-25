import pandas as pd

INPUT_FILE = "data_pipeline/books_raw.csv"
OUTPUT_FILE = "data_pipeline/books_cleaned.csv"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def clean_data(df):
    df = df.copy()

    df["price_gbp"] = (
        df["price_gbp"]
        .astype(str)
        .str.replace("Â", "", regex=False)
        .str.replace("£", "", regex=False)
        .str.strip()
    )

    df["price_gbp"] = pd.to_numeric(
        df["price_gbp"],
        errors="coerce"
    )

    df["star_rating"] = df["star_rating"].map(RATING_MAP)

    df["in_stock"] = (
        df["availability"]
        .astype(str)
        .str.contains("In stock", case=False, na=False)
    )

    df = df.drop(columns=["availability"])

    df["category"] = df["category"].astype(str).str.strip()

    df = df.dropna(
        subset=["title", "price_gbp", "star_rating", "category"]
    )

    df["price_inr"] = df["price_gbp"] * 105.50

    return df

if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE)

    cleaned_df = clean_data(df)

    cleaned_df.to_csv(OUTPUT_FILE, index=False)

    print("Cleaned dataset shape:", cleaned_df.shape)
    print("\nData types:")
    print(cleaned_df.dtypes)
    print("\nFirst 5 rows:")
    print(cleaned_df.head())
    print("\nCleaned data saved successfully.")