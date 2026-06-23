import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

CSV_FILES = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 60)
print("DATA INGESTION")
print("=" * 60)

for file in CSV_FILES:
    df = pd.read_csv(RAW_DIR / file)

    print(f"\n{file}")
    print("Shape:", df.shape)

    nulls = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print("Null Values:", nulls)
    print("Duplicates:", duplicates)

print("\nData ingestion completed.")