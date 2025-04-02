import pandas as pd

# Define the file paths
train_file_path = "train-00000-of-00001.parquet"
test_file_path = "test-00000-of-00001.parquet"

# Read the parquet files into DataFrames
train_df = pd.read_parquet(train_file_path)
test_df = pd.read_parquet(test_file_path)

# Check the first few rows of each DataFrame
print(train_df.head())
print(test_df.head())
