import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

PROCESSED_DIR = Path("data/processed")

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
    "dim_fund": "fund_master_clean.csv",
    "fact_nav": "nav_history_clean.csv",
    "fact_aum": "aum_clean.csv",
    "fact_sip": "sip_clean.csv",
    "fact_category_inflows": "category_inflows_clean.csv",
    "fact_folio": "folio_clean.csv",
    "fact_performance": "scheme_performance_clean.csv",
    "fact_transactions": "investor_transactions_clean.csv",
    "fact_portfolio": "portfolio_holdings_clean.csv",
    "fact_benchmark": "benchmark_indices_clean.csv"
}

for table, file in files.items():

    df = pd.read_csv(
        PROCESSED_DIR / file
    )

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table}: {len(df)} rows"
    )

print("SQLite load complete.")
