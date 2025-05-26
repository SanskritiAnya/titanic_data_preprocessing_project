import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv(r'C:\Users\KIIT\Downloads\titanic-dataset.zip.zip')

#columns to scale
num_cols = ['Age', 'Fare', 'SibSp', 'Parch', 'Pclass']

#initializing scalers
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

#normalising numerical columns (scale between 0 and 1)
df_norm = df.copy()
df_norm[num_cols] = min_max_scaler.fit_transform(df[num_cols])

print("Normalized Data:")
print(df_norm[num_cols].head())

#standardizing numerical columns (mean=0, std=1)
df_std = df.copy()
df_std[num_cols] = standard_scaler.fit_transform(df[num_cols])

print("\nStandardized Data:")
print(df_std[num_cols].head())
