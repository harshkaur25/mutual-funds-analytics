from sqlalchemy import create_engine
import pandas as pd

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
tx = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
perf = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Save to SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
tx.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database loaded successfully!")
print("Tables created:")
print("- fact_nav")
print("- fact_transactions")
print("- fact_performance")