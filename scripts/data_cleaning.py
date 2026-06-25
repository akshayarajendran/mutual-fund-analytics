import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)


nav = pd.read_csv("data/raw/02_nav_history.csv")


nav["date"] = pd.to_datetime(nav["date"])


nav = nav.sort_values(["amfi_code", "date"])


nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV History cleaned successfully")

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)


transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)


transactions = transactions[
    transactions["amount_inr"] > 0
]


valid_kyc = ["Verified", "Pending", "Rejected"]

transactions = transactions[
    transactions["kyc_status"].isin(valid_kyc)
]

transactions = transactions.drop_duplicates()

transactions.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Investor Transactions cleaned successfully")


performance = pd.read_csv("data/raw/07_scheme_performance.csv")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
]

for col in return_columns:
    performance[col] = pd.to_numeric(
        performance[col],
        errors="coerce"
    )


performance["expense_ratio_flag"] = (
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
)

performance = performance.drop_duplicates()

performance.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Scheme Performance cleaned successfully")