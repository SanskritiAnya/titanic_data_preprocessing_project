import pandas as pd

df = pd.read_csv(r'C:\Users\KIIT\Downloads\titanic-dataset.zip.zip')  

# encoding 'Sex' column: male : 0, female : 1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

#printing the first 5 rows to verify encoding
print(df.head())
