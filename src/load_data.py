import pandas as pd 
df = pd.read_csv("data/raw/01_fund_master.csv")
print("shape")
print(df.shape)
print("\nColumns")
print(df.columns)
print("\nMIssing Values")
print(df.isnull().sum())