def estimate_revenue_uplift(monthly_users: int, baseline_rate: float, improved_rate: float, avg_order_value: float) -> dict:
    baseline_conversions = monthly_users * baseline_rate
    improved_conversions = monthly_users * improved_rate
    incremental_conversions = improved_conversions - baseline_conversions
    incremental_revenue = incremental_conversions * avg_order_value

    return {
        "baseline_conversions": round(baseline_conversions),
        "improved_conversions": round(improved_conversions),
        "incremental_conversions": round(incremental_conversions),
        "incremental_revenue": round(incremental_revenue, 2)
    }

if __name__ == "__main__":
    result = estimate_revenue_uplift(
        monthly_users=100000,
        baseline_rate=0.05,
        improved_rate=0.062,
        avg_order_value=60
    )
    print(result)
