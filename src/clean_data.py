import pandas as pd

INPUT = "data/raw/online_retail_raw.csv"
OUTPUT = "data/processed/online_retail_cleaned.csv"

def clean_data():
    df = pd.read_csv(INPUT)

    print("Raw shape:", df.shape)

    # Standardize column names
    df.columns = [col.strip() for col in df.columns]

    # Remove rows with missing customer IDs
    df = df.dropna(subset=["CustomerID"])

    # Remove cancellation invoices
    df = df[~df["InvoiceNo"].astype(str).str.startswith(("C", "c"))]

    # Keep only positive quantity and price
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Parse dates
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    # Drop rows with invalid dates
    df = df.dropna(subset=["InvoiceDate"])

    # Remove exact duplicates
    df = df.drop_duplicates()

    # Create revenue column
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Normalize customer id
    df["CustomerID"] = df["CustomerID"].astype(str).str.replace(".0", "", regex=False)

    df.to_csv(OUTPUT, index=False)

    print("Cleaned shape:", df.shape)
    print("Saved to:", OUTPUT)
    print("\nNull counts:")
    print(df.isnull().sum())
    print("\nDate range:")
    print(df["InvoiceDate"].min(), "to", df["InvoiceDate"].max())
    print("\nRevenue summary:")
    print(df["TotalPrice"].describe())

if __name__ == "__main__":
    clean_data()
