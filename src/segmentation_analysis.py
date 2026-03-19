import os
import pandas as pd

INPUT = "data/processed/customer_summary.csv"
OUTPUT = "outputs/tables/customer_segment_summary.csv"

def run_segmentation():
    os.makedirs("outputs/tables", exist_ok=True)

    df = pd.read_csv(INPUT)

    summary = (
        df.groupby("repeat_customer_flag")
          .agg(
              customers=("CustomerID", "count"),
              avg_revenue=("total_revenue", "mean"),
              median_revenue=("total_revenue", "median"),
              avg_orders=("invoice_count", "mean"),
              avg_recency_days=("recency_days", "mean")
          )
          .reset_index()
    )

    summary["segment"] = summary["repeat_customer_flag"].map({
        0: "One-time customers",
        1: "Repeat customers"
    })

    summary = summary[[
        "segment",
        "customers",
        "avg_revenue",
        "median_revenue",
        "avg_orders",
        "avg_recency_days"
    ]]

    summary.to_csv(OUTPUT, index=False)

    print("Saved:", OUTPUT)
    print(summary)

if __name__ == "__main__":
    run_segmentation()
