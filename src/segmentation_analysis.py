import pandas as pd

def segment_conversion_summary(
    df: pd.DataFrame,
    segment_col: str,
    converted_col: str
) -> pd.DataFrame:
    summary = (
        df.groupby(segment_col)
          .agg(
              users=(converted_col, "count"),
              conversions=(converted_col, "sum")
          )
          .reset_index()
    )
    summary["conversion_rate_pct"] = (summary["conversions"] / summary["users"] * 100).round(2)
    return summary.sort_values("conversion_rate_pct", ascending=False)

if __name__ == "__main__":
    print("Segmentation analysis starter ready.")
