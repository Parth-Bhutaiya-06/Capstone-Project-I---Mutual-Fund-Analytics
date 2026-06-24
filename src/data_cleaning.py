import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# FUND MASTER

fund_master = pd.read_csv(RAW_DIR / "01_fund_master.csv")

fund_master.columns = fund_master.columns.str.strip().str.lower()
fund_master.drop_duplicates(inplace=True)

fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"],
    errors="coerce"
)

fund_master.to_csv(
    PROCESSED_DIR / "fund_master_clean.csv",
    index=False
)

# NAV HISTORY

nav = pd.read_csv(RAW_DIR / "02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav.dropna(subset=["date"], inplace=True)

nav.sort_values(
    ["amfi_code", "date"],
    inplace=True
)

nav.drop_duplicates(inplace=True)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav[nav["nav"] > 0]

nav.to_csv(
    PROCESSED_DIR / "nav_history_clean.csv",
    index=False
)

# AUM

aum = pd.read_csv(RAW_DIR / "03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum.drop_duplicates(inplace=True)

aum.to_csv(
    PROCESSED_DIR / "aum_clean.csv",
    index=False
)

# SIP INFLOWS

sip = pd.read_csv(
    RAW_DIR / "04_monthly_sip_inflows.csv"
)

sip.drop_duplicates(inplace=True)

sip.to_csv(
    PROCESSED_DIR / "sip_clean.csv",
    index=False
)

# CATEGORY INFLOWS

category = pd.read_csv(
    RAW_DIR / "05_category_inflows.csv"
)

category.drop_duplicates(inplace=True)

category.to_csv(
    PROCESSED_DIR / "category_inflows_clean.csv",
    index=False
)

# FOLIOS

folio = pd.read_csv(
    RAW_DIR / "06_industry_folio_count.csv"
)

folio.drop_duplicates(inplace=True)

folio.to_csv(
    PROCESSED_DIR / "folio_clean.csv",
    index=False
)

# SCHEME PERFORMANCE

perf = pd.read_csv(
    RAW_DIR / "07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

anomalies = perf[
    (perf["return_1yr_pct"] > 100)
    | (perf["return_1yr_pct"] < -50)
]

anomalies.to_csv(
    PROCESSED_DIR / "performance_anomalies.csv",
    index=False
)

perf = perf[
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
]

perf.to_csv(
    PROCESSED_DIR / "scheme_performance_clean.csv",
    index=False
)

# INVESTOR TRANSACTIONS

txn = pd.read_csv(
    RAW_DIR / "08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.upper()
    .str.strip()
)

mapping = {
    "SIP": "SIP",
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "LUMPSUM": "LUMPSUM",
    "ONE TIME": "LUMPSUM",
    "REDEMPTION": "REDEMPTION"
}

txn["transaction_type"] = (
    txn["transaction_type"]
    .replace(mapping)
)

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "VERIFIED",
    "PENDING",
    "REJECTED"
]

txn["kyc_status"] = (
    txn["kyc_status"]
    .astype(str)
    .str.upper()
)

txn = txn[
    txn["kyc_status"]
    .isin(valid_kyc)
]

txn.to_csv(
    PROCESSED_DIR /
    "investor_transactions_clean.csv",
    index=False
)

# PORTFOLIO

portfolio = pd.read_csv(
    RAW_DIR / "09_portfolio_holdings.csv"
)

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"],
    errors="coerce"
)

portfolio.drop_duplicates(inplace=True)

portfolio.to_csv(
    PROCESSED_DIR /
    "portfolio_holdings_clean.csv",
    index=False
)

# BENCHMARK

benchmark = pd.read_csv(
    RAW_DIR / "10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"],
    errors="coerce"
)

benchmark.drop_duplicates(inplace=True)

benchmark.to_csv(
    PROCESSED_DIR /
    "benchmark_indices_clean.csv",
    index=False
)

print("All datasets cleaned successfully.")