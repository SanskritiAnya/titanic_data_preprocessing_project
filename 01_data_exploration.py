import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv("titanic-dataset.zip")

# Displaying the first 5 rows
print("First few rows of the dataset:")
print(df.head())

# Displaying data types and non-null counts
print("\n Dataset Info:")
print(df.info())

# Checking for missing values in each column
print("\n Missing values in each column:")
print(df.isnull().sum())
