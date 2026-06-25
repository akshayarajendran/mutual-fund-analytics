import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database loaded successfully.")