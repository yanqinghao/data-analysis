import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/1串.csv", index_col=0)
cols = [
    '时间', '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib', 'Uc', 'Ic', 'Pac', 'cosφ',
    'Qpy', 'Qdc', 'Qac', 'Eff '
]
print(len(df))
df = df[df['辐照度'] < 2000]
print(len(df))
df = df[df['Pdc'] < 10000]
print(len(df))
df = df[df['Pac'] < 10000]
print(len(df))
for col in cols:
    if col != '时间':
        plt.clf()
        plt.hist(x=df[col].values, bins=100)
        plt.savefig("images/" + col + "hist.png")
