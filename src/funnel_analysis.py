import pandas as pd

def calculate_funnel(df: pd.DataFrame, user_col: str, stage_col: str, stage_order: list[str]) -> pd.DataFrame:
    funnel_rows = []

    for stage in stage_order:
        users_at_stage = df.loc[df[stage_col] == stage, user_col].nunique()
        funnel_rows.append({"stage": stage, "users": users_at_stage})

    funnel_df = pd.DataFrame(funnel_rows)
    funnel_df["drop_off_from_previous"] = funnel_df["users"].shift(1) - funnel_df["users"]
    funnel_df["conversion_from_previous_pct"] = (funnel_df["users"] / funnel_df["users"].shift(1) * 100).round(2)
    funnel_df["overall_conversion_pct"] = (funnel_df["users"] / funnel_df["users"].iloc[0] * 100).round(2)

    return funnel_df

if __name__ == "__main__":
    print("Funnel analysis starter ready.")
