import pandas as pd

# Load performance data

perf = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
).strip().title()

# Mapping

risk_map = {
    "Low": ["Low"],
    "Moderate": ["Moderate"],
    "High": ["High", "Very High"]
}

if risk not in risk_map:
    print("Invalid Risk Appetite")
    exit()

# Filter

filtered = perf[
    perf["risk_grade"].isin(
        risk_map[risk]
    )
]

# Top 3 Sharpe

recommendations = (
    filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop Fund Recommendations\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "sharpe_ratio",
            "risk_grade"
        ]
    ]
)