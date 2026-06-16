
import pandas as pd

df = pd.read_excel('Raw_Dataset.xlsx')
df['Sales'] = df['Sales'].fillna(df['Sales'].median())
df['Region'] = df['Region'].fillna('Unknown').replace({'north':'North'})
df = df.drop_duplicates()
df.to_excel('Cleaned_Dataset.xlsx', index=False)

print('Data cleaning completed successfully')
