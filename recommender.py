'''import pandas as pd

# Load scheme performance data
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Ask user for risk appetite
risk = input("Enter Risk Appetite (Low / Moderate / High): ")

# Filter funds based on risk
filtered = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

# Top 3 funds by Sharpe Ratio
top3 = filtered.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds:\n")

print(
    top3[
        [
            "scheme_name",
            "risk_grade",
            "sharpe_ratio",
            "annual_return"
        ]
    ]
)
performance = pd.read_csv("../data/processed/07_scheme_performance_cleaned.csv")
print(performance.columns.tolist())'''
import pandas as pd

# Load the scheme performance dataset
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Ask user for risk appetite
risk = input("Enter Risk Appetite (Low / Moderate / High): ")

# Filter funds based on risk grade
filtered = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

# Check if any funds match the risk level
if filtered.empty:
    print("No funds found for the selected risk appetite.")
else:
    # Select top 3 funds by Sharpe Ratio
    top3 = filtered.sort_values(
        by="sharpe_ratio",
        ascending=False
    ).head(3)

    print("\nTop 3 Recommended Funds:\n")

    print(
        top3[
            [
                "scheme_name",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ]
    )