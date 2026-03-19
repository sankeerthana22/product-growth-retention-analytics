import os
import pandas as pd

INPUT = "data/processed/customer_summary.csv"
OUTPUT = "outputs/tables/revenue_concentration_summary.csv"

def run_revenue_impact():
    os.makedirs("outputs/tables", exist_ok=True)

    df = pd.read_csv(INPUT)
    df = df.sort_values("total_revenue", ascending=False).reset_index(drop=True)

    total_revenue = df["total_revenue"].sum()

    top_10_pct_n = max(1, int(len(df) * 0.10))
    top_20_pct_n = max(1, int(len(df) * 0.20))

    top_10_revenue_share = df.head(top_10_pct_n)["total_revenue"].sum() / total_revenue * 100
    top_20_revenue_share = df.head(top_20_pct_n)["total_revenue"].sum() / total_revenue * 100
    repeat_customer_share = df[df["repeat_customer_flag"] == 1]["total_revenue"].sum() / total_revenue * 100

    summary = pd.DataFrame({
        "metric": [
            "Top 10% customer revenue share",
            "Top 20% customer revenue share",
            "Repeat customer revenue share"
        ],
        "value_pct": [
            round(top_10_revenue_share, 2),
            round(top_20_revenue_share, 2),
            round(repeat_customer_share, 2)
        ]
    })

    summary.to_csv(OUTPUT, index=False)

    print("Saved:", OUTPUT)
    print(summary)

if __name__ == "__main__":
    run_revenue_impact()
