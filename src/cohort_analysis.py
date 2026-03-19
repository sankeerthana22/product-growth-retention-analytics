import os
import pandas as pd

INPUT = "data/processed/online_retail_cleaned.csv"
OUTPUT = "outputs/tables/cohort_retention.csv"

def build_cohort():
    os.makedirs("outputs/tables", exist_ok=True)

    df = pd.read_csv(INPUT, parse_dates=["InvoiceDate"])

    df["invoice_month"] = df["InvoiceDate"].dt.to_period("M")
    df["cohort_month"] = df.groupby("CustomerID")["invoice_month"].transform("min")

    df["cohort_index"] = (
        (df["invoice_month"].dt.year - df["cohort_month"].dt.year) * 12 +
        (df["invoice_month"].dt.month - df["cohort_month"].dt.month) + 1
    )

    cohort_data = (
        df.groupby(["cohort_month", "cohort_index"])["CustomerID"]
          .nunique()
          .reset_index()
          .rename(columns={"CustomerID": "active_customers"})
    )

    cohort_size = (
        cohort_data[cohort_data["cohort_index"] == 1][["cohort_month", "active_customers"]]
        .rename(columns={"active_customers": "cohort_size"})
    )

    cohort = cohort_data.merge(cohort_size, on="cohort_month", how="left")
    cohort["retention_rate_pct"] = (cohort["active_customers"] / cohort["cohort_size"] * 100).round(2)

    cohort.to_csv(OUTPUT, index=False)

    print("Saved:", OUTPUT)
    print(cohort.head(20))

if __name__ == "__main__":
    build_cohort()
