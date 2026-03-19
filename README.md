# Product Growth & Retention Analytics

An end-to-end data analytics project focused on identifying user drop-off, segment-level conversion differences, retention behavior, and experiment-driven conversion improvement opportunities.

## Business Problem

An e-commerce business wants to improve conversion and revenue. However, users are dropping off before completing key actions. This project investigates the customer journey, identifies high-friction segments, evaluates retention over time, and assesses whether a product change improved conversion performance.

## Project Objectives

- Measure user drop-off across the funnel
- Compare conversion behavior across user segments
- Evaluate retention trends through cohort analysis
- Assess experiment results using A/B testing
- Translate findings into business recommendations and revenue impact

## Analysis Components

### 1. Funnel Analysis
Used to identify where users are dropping off in the journey.

### 2. Segmentation Analysis
Used to determine which user groups perform differently.

### 3. Cohort Analysis
Used to evaluate whether users are retained over time.

### 4. A/B Test Analysis
Used to validate whether a product change improved conversion significantly.

### 5. Revenue Impact
Used to estimate the business value of conversion improvements.

## Tools
- Python
- SQL
- SQLite
- Pandas
- NumPy
- Matplotlib
- SciPy / Statsmodels

## Folder Structure

```bash
product-growth-retention-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── sql/
├── src/
├── analysis/
├── outputs/
│   ├── charts/
│   └── tables/
├── docs/
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore

---

# Step 7 — Add starter Python loader

Run:

```bash
cat > src/load_data.py <<'EOF'
import os
import pandas as pd

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

def load_csv(filename: str) -> pd.DataFrame:
    path = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(path)
    print(f"Loaded {filename}: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    files = os.listdir(RAW_DIR)
    if not files:
        print("No raw data files found in data/raw")
    else:
        for f in files:
            if f.endswith(".csv"):
                load_csv(f)
