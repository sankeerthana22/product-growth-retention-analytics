import pandas as pd

INPUT = "data/processed/online_retail_cleaned.csv"
OUTPUT = "data/processed/customer_summary.csv"

def build_customer_summary():
    df = pd.read_csv(INPUT, parse_dates=["InvoiceDate"])

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    customer = (
        df.groupby("CustomerID")
          .agg(
              first_purchase=("InvoiceDate", "min"),
              last_purchase=("InvoiceDate", "max"),
              invoice_count=("InvoiceNo", "nunique"),
              total_units=("Quantity", "sum"),
              total_revenue=("TotalPrice", "sum"),
              avg_line_revenue=("TotalPrice", "mean"),
              country=("Country", lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
          )
          .reset_index()
    )

    customer["recency_days"] = (snapshot_date - customer["last_purchase"]).dt.days
    customer["customer_lifespan_days"] = (customer["last_purchase"] - customer["first_purchase"]).dt.days
    customer["repeat_customer_flag"] = (customer["invoice_count"] > 1).astype(int)

    revenue_q75 = customer["total_revenue"].quantile(0.75)
    customer["high_value_flag"] = (customer["total_revenue"] >= revenue_q75).astype(int)

    customer.to_csv(OUTPUT, index=False)

    print("Saved:", OUTPUT)
    print("Shape:", customer.shape)
    print("\nRepeat customer distribution:")
    print(customer["repeat_customer_flag"].value_counts(dropna=False))
    print("\nRevenue summary:")
    print(customer["total_revenue"].describe())

if __name__ == "__main__":
    build_customer_summary()
