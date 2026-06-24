import pandas as pd

# ==================================
# 1. CLEAN NAV HISTORY
# ==================================

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("NAV History cleaned")


# ==================================
# 2. CLEAN INVESTOR TRANSACTIONS
# ==================================

tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.upper()
)

tx["transaction_type"] = (
    tx["transaction_type"]
    .replace({
        "SIP": "SIP",
        "LUMPSUM": "Lumpsum",
        "REDEMPTION": "Redemption"
    })
)

tx = tx[tx["amount_inr"] > 0]

print("KYC Values:")
print(tx["kyc_status"].unique())

tx.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions cleaned")


# ==================================
# 3. CLEAN SCHEME PERFORMANCE
# ==================================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance cleaned")

print("All cleaning completed!")