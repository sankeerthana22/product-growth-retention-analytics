# Customer Retention & Revenue Analytics for Online Retail

An end-to-end data analytics project using Python and SQL-style analytical thinking to evaluate customer purchase behavior, repeat buying patterns, retention dynamics, and revenue concentration for an online retail business.

## Business Problem

Online retailers often grow revenue without understanding whether performance is driven by healthy repeat-purchase behavior or by a narrow group of high-value customers. This project analyzes transactional retail data to identify customer value patterns, retention weaknesses, and revenue concentration risk.

## Objectives

- Clean and prepare messy real-world transactional data
- Build a customer-level analytical dataset from raw line-item transactions
- Compare one-time vs repeat customer behavior
- Measure retention patterns through cohort analysis
- Evaluate how much revenue is concentrated among top customer groups
- Translate findings into business recommendations for growth and retention

## Dataset

This project uses the UCI Online Retail dataset, a real transactional dataset from a UK-based online retailer covering December 2010 through December 2011.

## Data Cleaning

The raw dataset contained missing customer IDs, cancellations, invalid quantities or prices, and duplicate records. Cleaning steps included:

- removing rows with missing `CustomerID`
- excluding cancellation invoices
- filtering out non-positive quantity and unit price records
- parsing transaction timestamps
- removing exact duplicates
- creating a `TotalPrice` revenue field

## Analytical Layers

### 1. Transaction-Level Cleaning
Prepared analysis-ready line-item retail data from raw records.

### 2. Customer-Level Summary
Aggregated transactions into one row per customer with:
- first and last purchase dates
- invoice count
- total units purchased
- total revenue
- recency
- customer lifespan
- repeat customer flag
- high-value customer flag

### 3. Segmentation Analysis
Compared one-time vs repeat customers on:
- customer counts
- average revenue
- median revenue
- average orders
- average recency

### 4. Cohort Retention Analysis
Tracked customer activity by acquisition month and measured retention across later month indices.

### 5. Revenue Concentration Analysis
Measured the revenue share contributed by top customer groups to understand concentration risk.

## Key Findings

- Repeat customers represented **65.58%** of the customer base but generated **93.09%** of total revenue, making repeat purchase behavior the strongest long-term growth driver.
- Revenue was highly concentrated: the top **10%** of customers contributed **61.41%** of revenue, while the top **20%** contributed **74.66%**, indicating meaningful dependency on a relatively small customer segment.
- One-time customers generated far lower value than repeat buyers, with average revenue of **411.25** compared with **2907.99** for repeat customers.
- Retention weakened quickly after acquisition, with average month-2 retention of **20.62%**, highlighting post-purchase engagement as the main area for improvement.

## Business Recommendations

- Prioritize retention strategies for first-time buyers, since repeat customers generate outsized value.
- Build lifecycle campaigns targeting customers shortly after first purchase to improve month-2 retention.
- Focus commercial attention on high-value customer segments because revenue concentration suggests a small group drives disproportionate business impact.
- Monitor repeat purchase behavior as a core KPI, not just total revenue, to improve long-term revenue stability.

## Key Outputs

- `data/processed/online_retail_cleaned.csv`
- `data/processed/customer_summary.csv`
- `outputs/tables/customer_segment_summary.csv`
- `outputs/tables/cohort_retention.csv`
- `outputs/tables/revenue_concentration_summary.csv`
- `analysis/business_summary.md`

## Visual Outputs

- `outputs/charts/avg_revenue_by_segment.png`
- `outputs/charts/revenue_concentration_summary.png`
- `outputs/charts/avg_cohort_retention_trend.png`

## Business Value

This project demonstrates how customer analytics can be used to:
- identify the value gap between one-time and repeat buyers
- detect retention drop-off after the first purchase
- measure revenue concentration among top customers
- prioritize retention and lifecycle strategies to improve long-term revenue stability

## Tools

- Python
- Pandas
- Matplotlib
- CSV-based analytics pipeline
- Customer segmentation
- Cohort analysis

## Project Structure

```bash
product-growth-retention-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
├── sql/
├── outputs/
│   ├── charts/
│   └── tables/
├── analysis/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore



## Additional SQL Insights

- Revenue was highly concentrated geographically, with the United Kingdom contributing **.29M** in revenue across **3,920** customers, far exceeding all other countries.
- Monthly revenue fluctuated over time, with stronger performance in **May 2011 (.36K)** and **June 2011 (.05K)** compared with **February 2011 (.08K)**, suggesting seasonality or uneven purchasing cycles.
- Customer revenue concentration was also visible at the individual level: the top customer generated **.21K**, reinforcing the finding that a small subset of customers drives disproportionate business value.
