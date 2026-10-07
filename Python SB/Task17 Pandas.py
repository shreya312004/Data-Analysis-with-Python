"Module :- Pandas"
"description:- Pandas operations"

import pandas as pd

df = pd.read_csv('healthcare_dataset.csv')

print(df)

print('\n-----Data Display-----')
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

print('\n------Handling Missing Values')
print(df.isnull())
print(df.isnull().sum())
print(df.drop_duplicates)