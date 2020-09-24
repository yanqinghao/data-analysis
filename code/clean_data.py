import pandas as pd

df = pd.read_csv("data/1串.csv", index_col=0)
print(len(df))
df = df[(df['辐照度'] < 2000) & (df['辐照度'] > 0)]
print(len(df))
df = df[(df['Pdc'] < 10000) & (df['Pdc'] > 0)]
print(len(df))
df = df[df['Pac'] < 10000]
print(len(df))
df = df[df['cosφ'] < 10000]
print(len(df))
df = df[df['Ic'] < 10000]
print(len(df))
df = df[df['Uc'] < 10000]
print(len(df))
df = df[df['Udc'] > 400]
print(len(df))
df.to_csv("data/1串.csv")
df.describe().to_csv("data/describe_1.csv")
