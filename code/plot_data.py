import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv("data/1串.csv", index_col=0)
# df.describe().to_csv("data/describe_1.csv")
# cols = [
#     '时间', '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib', 'Uc', 'Ic', 'Pac', 'cosφ',
#     'Qpy', 'Qdc', 'Qac', 'Eff '
# ]
# for col in cols:
#     if col != '时间':
#         plt.clf()
#         plt.hist(x=df[col].values, bins=100)
#         plt.savefig("images/" + col + "hist.png")
results = ["data/每年统计.csv", "data/每日统计.csv", "data/每月统计.csv"]
for res in results:
    df = pd.read_csv(res)
    x = list(df.columns)
    df.describe().to_csv("data/describe_1.csv")
    cols = [
        '时间', '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib', 'Uc', 'Ic', 'Pac',
        'cosφ', 'Qpy', 'Qdc', 'Qac', 'Eff '
    ]
    for col in cols:
        if col != '时间':
            plt.clf()
            plt.plot(x1, y1, label="line 1")
            plt.savefig("images/" + col + "hist.png")
