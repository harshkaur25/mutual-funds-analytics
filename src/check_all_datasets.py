import pandas as pd 
import os 
folder = "data/raw"
for file in os.listdir(folder):
    if file.endswith(".csv"):
        path = os.path.join(folder , file)
        df = pd.read_csv(path)
        print("\n" + "="*50)
        print("dataset:",file)
        print("shape:",df.shape)
        print("missing value:")
        print(df.isnull().sum().sum())