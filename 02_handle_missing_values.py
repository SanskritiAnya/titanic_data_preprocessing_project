import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\titanic-dataset.zip.zip')  # Replace with your CSV file path

# Checking missing values before handling
print("Missing values before handling:")
print(df.isnull().sum())

# handling missing values

#filling missing Age with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# dropping Cabin column (too many missing values)
df.drop('Cabin', axis=1, inplace=True)

# filling missing Embarked with mode (most common value)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# checking missing values after handling
print("\nMissing values after handling:")
print(df.isnull().sum())

