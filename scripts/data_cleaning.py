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

# -------------------------------
# 4. Clean fund_master.csv
# -------------------------------
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"]
)

fund_master = fund_master.drop_duplicates()

fund_master.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("Fund Master cleaned successfully")


# -------------------------------
# 5. Clean aum_by_fund_house.csv
# -------------------------------
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum["date"] = pd.to_datetime(
    aum["date"]
)

aum = aum.drop_duplicates()

aum.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("AUM by Fund House cleaned successfully")


# -------------------------------
# 6. Clean monthly_sip_inflows.csv
# -------------------------------
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

sip["month"] = pd.to_datetime(
    sip["month"]
)

sip = sip.drop_duplicates()

sip.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("Monthly SIP Inflows cleaned successfully")


# -------------------------------
# 7. Clean category_inflows.csv
# -------------------------------
category = pd.read_csv("data/raw/05_category_inflows.csv")

category["month"] = pd.to_datetime(
    category["month"]
)

category = category.drop_duplicates()

category.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)

print("Category Inflows cleaned successfully")


# -------------------------------
# 8. Clean industry_folio_count.csv
# -------------------------------
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")

folio["month"] = pd.to_datetime(
    folio["month"]
)

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)

print("Industry Folio Count cleaned successfully")


# -------------------------------
# 9. Clean portfolio_holdings.csv
# -------------------------------
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

portfolio["portfolio_date"] = pd.to_datetime(
    portfolio["portfolio_date"]
)

portfolio = portfolio.drop_duplicates()

portfolio.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("Portfolio Holdings cleaned successfully")


# -------------------------------
# 10. Clean benchmark_indices.csv
# -------------------------------
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)

print("Benchmark Indices cleaned successfully")