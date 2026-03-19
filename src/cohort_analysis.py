import pandas as pd

def build_monthly_cohort(df: pd.DataFrame, user_col: str, order_date_col: str) -> pd.DataFrame:
    cohort_df = df.copy()
    cohort_df[order_date_col] = pd.to_datetime(cohort_df[order_date_col])

    cohort_df["order_month"] = cohort_df[order_date_col].dt.to_period("M")
    cohort_df["cohort_month"] = cohort_df.groupby(user_col)["order_month"].transform("min")

    cohort_df["cohort_index"] = (
        (cohort_df["order_month"].dt.year - cohort_df["cohort_month"].dt.year) * 12 +
        (cohort_df["order_month"].dt.month - cohort_df["cohort_month"].dt.month) + 1
    )

    grouped = (
        cohort_df.groupby(["cohort_month", "cohort_index"])[user_col]
        .nunique()
        .reset_index()
        .rename(columns={user_col: "active_users"})
    )

    cohort_sizes = grouped[grouped["cohort_index"] == 1][["cohort_month", "active_users"]]
    cohort_sizes = cohort_sizes.rename(columns={"active_users": "cohort_size"})

    retention = grouped.merge(cohort_sizes, on="cohort_month")
    retention["retention_rate_pct"] = (retention["active_users"] / retention["cohort_size"] * 100).round(2)

    return retention

if __name__ == "__main__":
    print("Cohort analysis starter ready.")
