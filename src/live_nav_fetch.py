import requests
import pandas as pd
import os

schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

output_folder = "data/raw"

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    
    response = requests.get(url)
    data = response.json()

    # NAV data is inside 'data' key
    nav_data = data["data"]

    df = pd.DataFrame(nav_data)

    file_path = os.path.join(output_folder, f"{name}_nav.csv")
    df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")