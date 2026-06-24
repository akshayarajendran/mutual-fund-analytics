import requests
import pandas as pd

schemes = {
"sbi_bluechip": 119551,
"icici_bluechip": 120503,
"nippon_large_cap": 118632,
"axis_bluechip": 119092,
"kotak_bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{name}.csv"

    nav_df.to_csv(file_name, index=False)

    print(f"Saved: {file_name}")

