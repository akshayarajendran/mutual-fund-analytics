import pandas as pd
import os

DATA_PATH = "data/raw"
df = pd.read_csv("data/raw/10_benchmark_indices.csv")

print("Missing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)
# for file in os.listdir(DATA_PATH):

#     if file.endswith(".csv"):

#         file_path = os.path.join(DATA_PATH, file)

#         df = pd.read_csv(file_path)

#         print("\n" + "="*60)
#         print(f"Dataset: {file}")

#         print("\nShape:")
#         print(df.shape)

#         print("\nData Types:")
#         print(df.dtypes)

#         print("\nFirst 5 Rows:")
#         print(df.head())