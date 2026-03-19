import os
import pandas as pd

CUSTOMER_INPUT = "data/processed/customer_summary.csv"
SEGMENT_INPUT = "outputs/tables/customer_segment_summary.csv"
COHORT_INPUT = "outputs/tables/cohort_retention.csv"
REVENUE_INPUT = "outputs/tables/revenue_concentration_summary.csv"
OUTPUT = "analysis/business_summary.md"

def main():
    os.makedirs("analysis", exist_ok=True)

    customer = pd.read_csv(CUSTOMER_INPUT)
    segment = pd.read_csv(SEGMENT_INPUT)
    cohort = pd.read_csv(COHORT_INPUT)
    revenue = pd.read_csv(REVENUE_INPUT)

    total_customers = customer["CustomerID"].nunique()
    total_revenue = customer["total_revenue"].sum()
    repeat_share = (customer["repeat_customer_flag"].mean() * 100).round(2)

    one_time = segment[segment["segment"] == "One-time customers"].iloc[0]
    repeat = segment[segment["segment"] == "Repeat customers"].iloc[0]

    cohort_2 = cohort[cohort["cohort_index"] == 2]["retention_rate_pct"]
    cohort_3 = cohort[cohort["cohort_index"] == 3]["retention_rate_pct"]

    avg_month_2_retention = round(cohort_2.mean(), 2) if not cohort_2.empty else None
    avg_month_3_retention = round(cohort_3.mean(), 2) if not cohort_3.empty else None

    top10 = revenue.loc[revenue["metric"] == "Top 10% customer revenue share", "value_pct"].iloc[0]
    top20 = revenue.loc[revenue["metric"] == "Top 20% customer revenue share", "value_pct"].iloc[0]
    repeat_rev = revenue.loc[revenue["metric"] == "Repeat customer revenue share", "value_pct"].iloc[0]

    summary = f"""# Business Summary

## Dataset Scope
- Total customers analyzed: {total_customers:,}
- Total customer-level revenue captured: {total_revenue:,.2f}
- Repeat customer rate: {repeat_share:.2f}%

## Key Findings

### 1. Repeat customers are significantly more valuable
- One-time customers: {int(one_time['customers']):,} customers, average revenue {one_time['avg_revenue']:.2f}, median revenue {one_time['median_revenue']:.2f}, average orders {one_time['avg_orders']:.2f}
- Repeat customers: {int(repeat['customers']):,} customers, average revenue {repeat['avg_revenue']:.2f}, median revenue {repeat['median_revenue']:.2f}, average orders {repeat['avg_orders']:.2f}

### 2. Revenue is concentrated among a relatively small customer group
- Top 10% of customers contribute {top10:.2f}% of revenue
- Top 20% of customers contribute {top20:.2f}% of revenue
- Repeat customers contribute {repeat_rev:.2f}% of revenue

### 3. Retention declines after initial purchase
- Average month-2 retention across cohorts: {avg_month_2_retention if avg_month_2_retention is not None else 'N/A'}%
- Average month-3 retention across cohorts: {avg_month_3_retention if avg_month_3_retention is not None else 'N/A'}%

## Business Recommendations
1. Prioritize retention strategies for first-time buyers, since repeat customers generate outsized value.
2. Build lifecycle campaigns targeting customers shortly after first purchase to improve month-2 retention.
3. Focus commercial attention on high-value customer segments because revenue concentration suggests a small group drives disproportionate business impact.
4. Monitor repeat purchase behavior as a core KPI, not just total revenue, to improve long-term revenue stability.
"""

    with open(OUTPUT, "w") as f:
        f.write(summary)

    print(f"Saved: {OUTPUT}")
    print(summary)

if __name__ == "__main__":
    main()
