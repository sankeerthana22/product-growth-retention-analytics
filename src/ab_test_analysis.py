import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def run_ab_test(df: pd.DataFrame, group_col: str, converted_col: str) -> dict:
    summary = (
        df.groupby(group_col)[converted_col]
        .agg(["sum", "count"])
        .reset_index()
    )

    if summary.shape[0] != 2:
        raise ValueError("A/B test requires exactly two groups.")

    conversions = summary["sum"].values
    sample_sizes = summary["count"].values

    stat, p_value = proportions_ztest(conversions, sample_sizes)

    rates = (summary["sum"] / summary["count"] * 100).round(2).tolist()
    groups = summary[group_col].tolist()

    return {
        "groups": groups,
        "conversion_rates_pct": rates,
        "z_stat": float(stat),
        "p_value": float(p_value)
    }

if __name__ == "__main__":
    print("A/B test analysis starter ready.")
