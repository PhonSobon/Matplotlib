import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

# load data from CSV file
df1 = pd.read_csv(r"D:\Data Analytics\Data Visualization with Power BI\Score Student.csv")
df2 = pd.read_csv(r"D:\Data Analytics\Data Visualization with Power BI\Financial Sample.csv")

print(df2.head())
print(df1.shape)
print(df2.shape)

print(df1.info())
print(df2.info())

if df1.isnull().any().any() or df2.isnull().any().any():
    print('At least one of the DataFrames has null values')
else:
    print('Neither DataFrame has null values')

dfs = [df1, df2]
for df in dfs:
    for column in df.columns:
        new_column = column.replace(' ', '_').lower()
# rename the column in the dataframe
        df.rename(columns={column: new_column}, inplace=True)
print(df1.columns)
print(df2.columns)
uniq_count = df1['age'].nunique()
uniq_count

df1.drop(['gender', 'age', 'section'], axis=1, inplace=True)
