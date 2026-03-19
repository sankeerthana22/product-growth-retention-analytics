import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/charts", exist_ok=True)

# 1. Segment revenue comparison
seg = pd.read_csv("outputs/tables/customer_segment_summary.csv")
plt.figure(figsize=(8,5))
plt.bar(seg["segment"], seg["avg_revenue"])
plt.title("Average Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Revenue")
plt.tight_layout()
plt.savefig("outputs/charts/avg_revenue_by_segment.png")
plt.close()

# 2. Revenue concentration
rev = pd.read_csv("outputs/tables/revenue_concentration_summary.csv")
plt.figure(figsize=(8,5))
plt.bar(rev["metric"], rev["value_pct"])
plt.title("Revenue Concentration Summary")
plt.xlabel("Metric")
plt.ylabel("Revenue Share (%)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig("outputs/charts/revenue_concentration_summary.png")
plt.close()

# 3. Cohort retention trend (average by cohort_index)
cohort = pd.read_csv("outputs/tables/cohort_retention.csv")
avg_retention = cohort.groupby("cohort_index")["retention_rate_pct"].mean().reset_index()

plt.figure(figsize=(8,5))
plt.plot(avg_retention["cohort_index"], avg_retention["retention_rate_pct"], marker="o")
plt.title("Average Cohort Retention by Month Index")
plt.xlabel("Cohort Month Index")
plt.ylabel("Average Retention Rate (%)")
plt.tight_layout()
plt.savefig("outputs/charts/avg_cohort_retention_trend.png")
plt.close()

print("Saved charts to outputs/charts")
