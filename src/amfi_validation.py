import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Show basic info
print("Fund Master Shape:", fund_master.shape)
print("NAV History Shape:", nav_history.shape)

# Try finding common column (usually scheme code / amfi code)
print("\nFund Master Columns:", fund_master.columns)
print("\nNAV History Columns:", nav_history.columns)

# If AMFI code exists in both
if "amfi_code" in fund_master.columns and "amfi_code" in nav_history.columns:
    merged = fund_master.merge(nav_history, on="amfi_code", how="left")

    print("\nMerged Shape:", merged.shape)

    missing = merged[merged.isnull().any(axis=1)]
    print("\nMissing / Mismatch Records:", len(missing))
else:
    print("\nAMFI column not found directly — need mapping check")