# Product Growth & Retention Analytics

An end-to-end analytics project using real ecommerce transaction data to evaluate customer retention, repeat purchase behavior, and revenue concentration risk.

This analysis shows that growth is driven far more by **retaining repeat customers** than by relying only on new customer acquisition:

- **65.58%** of customers were repeat buyers
- Repeat customers generated **93.09%** of total revenue
- The **top 10%** of customers contributed **61.41%** of revenue
- Average **month-2 retention was only 20.62%**

## Executive Summary

This project analyzes transactional data from an online retail business to understand whether revenue growth is supported by healthy customer retention or overly dependent on a small set of valuable customers.

The analysis found that:

- revenue is highly concentrated among repeat and high-value customers
- one-time customers contribute materially less revenue than repeat buyers
- retention drops sharply after the first purchase
- the business faces concentration risk because a small customer segment drives a large share of revenue

### Strategic Conclusion

The highest-leverage growth opportunity is **improving early repeat purchase behavior**, not simply acquiring more one-time customers.

---

## Business Problem

Many ecommerce businesses grow top-line revenue without knowing:

- whether repeat customers are driving sustainable growth
- whether revenue is overly dependent on a small group of customers
- where retention weakens after acquisition

This project answers those questions by translating raw transaction data into customer-level insight.

## Business Questions

1. How much revenue is driven by repeat customers versus one-time buyers?
2. How concentrated is revenue among the highest-value customers?
3. Where does retention weaken across customer cohorts?
4. What actions should the business prioritize to improve growth quality?

---

## Dataset

**Source:** UCI Online Retail dataset  
**Type:** Real transactional ecommerce data  
**Period:** December 2010 to December 2011  
**Raw size:** 541,909 rows

The dataset contains invoice-level transaction records including:

- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

This is a strong real-world dataset for retention and customer analytics because it reflects actual purchasing behavior rather than synthetic or manually created records.

---

## Analytical Workflow

### 1. Data Cleaning

The raw data included several real-world issues:

- missing customer IDs
- cancellation invoices
- non-positive quantities or prices
- duplicate records

Cleaning steps included:

- removing rows with missing `CustomerID`
- excluding cancelled invoices
- filtering invalid quantity and unit price values
- parsing timestamps
- removing duplicates
- creating `TotalPrice = Quantity * UnitPrice`

### 2. Customer-Level Feature Engineering

Built a customer summary table with one row per customer, including:

- first purchase date
- last purchase date
- invoice count
- total units purchased
- total revenue
- recency
- customer lifespan
- repeat customer flag
- high-value customer flag

### 3. Segmentation Analysis

Compared one-time and repeat customers using:

- customer count
- average revenue
- median revenue
- average order count
- average recency

### 4. Cohort Retention Analysis

Measured monthly retention by acquisition cohort to identify where repeat behavior declines after first purchase.

### 5. Revenue Concentration Analysis

Quantified how much revenue is contributed by top customer groups to assess dependency risk.

### 6. SQL-Based Business Analysis

Used SQL to validate and extend findings through:

- top countries by revenue
- monthly revenue trend
- top customers by revenue

---

## Key Findings

### 1) Repeat Customers Are the Revenue Engine

- Repeat customers represented **65.58%** of customers
- Repeat customers generated **93.09%** of total revenue
- Average revenue per one-time customer: **411.25**
- Average revenue per repeat customer: **2907.99**

**Insight:** Repeat customers generated roughly **7x higher revenue** than one-time buyers.

### 2) Revenue Is Highly Concentrated

- Top **10%** of customers contributed **61.41%** of revenue
- Top **20%** of customers contributed **74.66%** of revenue

**Insight:** The business is meaningfully dependent on a relatively small group of high-value customers.

### 3) Retention Weakens Early

- Average **month-2 retention:** **20.62%**
- Average **month-3 retention:** **22.11%**

**Insight:** The biggest drop-off occurs soon after the first purchase, making early lifecycle engagement the most important retention lever.

### 4) Geographic Revenue Is Uneven

- The **United Kingdom** contributed **$7.29M** in revenue across **3,920** customers
- Other countries trailed significantly behind

**Insight:** Revenue concentration exists not only by customer segment, but also geographically.

### 5) Customer Concentration Is Visible at the Individual Level

- The top individual customer generated **$280.21K** in revenue

**Insight:** Losing a small number of top customers could have disproportionate revenue impact.

---

## Business Recommendations

### Priority 1: Improve First-to-Second Purchase Retention

The first 30–60 days after purchase are the highest-leverage intervention window.

Recommended actions:

- post-purchase email flows
- replenishment or reminder campaigns
- first-to-second purchase incentives
- cross-sell recommendations

### Priority 2: Protect High-Value Customers

Since a small customer segment drives most revenue, the business should prioritize:

- VIP segmentation
- loyalty and retention campaigns
- personalized engagement for high-value customers

### Priority 3: Track Retention-Focused KPIs

Total revenue alone can hide customer health. The business should monitor:

- repeat purchase rate
- cohort retention
- revenue share from repeat customers
- revenue concentration by top customer segments

---

## Dashboard

### Customer Revenue & Retention Dashboard

![Customer Revenue & Retention Dashboard](outputs/dashboard/customer_revenue_retention_dashboard.png)

This dashboard summarizes the final business findings:

- repeat customers drive the vast majority of revenue
- revenue is concentrated among a small share of customers
- retention is the main driver of long-term revenue stability

### Tableau Deliverables

- `outputs/dashboard/customer_revenue_retention_analysis.twbx`
- `outputs/dashboard/customer_revenue_retention_dashboard.png`

---

## Project Outputs

### Processed Data

- `data/processed/online_retail_cleaned.csv`
- `data/processed/customer_summary.csv`

### Analytical Tables

- `outputs/tables/customer_segment_summary.csv`
- `outputs/tables/cohort_retention.csv`
- `outputs/tables/revenue_concentration_summary.csv`
- `outputs/tables/top_10_countries_by_revenue.csv`
- `outputs/tables/monthly_revenue_trend.csv`
- `outputs/tables/top_20_customers_by_revenue.csv`

### Python Scripts

- `src/clean_data.py`
- `src/build_customer_summary.py`
- `src/segmentation_analysis.py`
- `src/cohort_analysis.py`
- `src/revenue_impact.py`
- `src/business_summary.py`
- `src/create_charts.py`

### SQL Files

- `sql/country_revenue_analysis.sql`
- `sql/customer_revenue_analysis.sql`
- `sql/monthly_revenue_analysis.sql`

---

## Tech Stack

- Python
- Pandas
- SQLite
- Matplotlib
- Customer segmentation
- Cohort retention analysis
- Revenue concentration analysis
- SQL business querying

---

## Repository Structure

    product-growth-retention-analytics/
    ├── analysis/
    ├── docs/
    ├── outputs/
    │   ├── dashboard/
    │   └── tables/
    ├── sql/
    ├── src/
    ├── README.md
    ├── requirements.txt
    └── .gitignore

---

## Limitations

This project is intentionally scoped to what the data can support.

- The dataset is transactional, not clickstream, so full funnel behavior is not available
- No acquisition channel or marketing source data is included
- The analysis is observational, not causal
- Missing customer IDs in the raw data were excluded during cleaning
- External drivers such as promotions, holidays, and pricing changes were not modeled directly

These limitations do not weaken the project; they clarify the scope of responsible interpretation.

---

## How to Run

1. Clean the raw data
2. Build the customer summary table
3. Generate segmentation, cohort, and revenue concentration outputs
4. Run SQL analyses for country, monthly, and customer revenue views
5. Review dashboard and output tables

---

## Final Takeaway

This project shows that strong analytics is not just about reporting revenue totals.

It is about identifying the business levers that actually matter.

For this business, the clearest conclusion is:

**Revenue growth depends far more on retaining and expanding repeat customer value than on simply adding more one-time buyers.**
