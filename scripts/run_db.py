import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT transaction_type,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()