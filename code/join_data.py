import pandas as pd

df1 = pd.read_csv("data/1组串_min.csv", index_col=0)
df2 = pd.read_csv("data/2组串_min.csv", index_col=0)
df3 = pd.read_csv("data/3组串_min.csv", index_col=0)
df4 = pd.read_csv("data/4组串_min.csv", index_col=0)
origin_cols = [
    '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib', 'Uc', 'Ic', 'Pac', 'cosφ',
    'Qpy', 'Qdc', 'Qac', 'Eff '
]
df2.columns = [col+"_2" for col in origin_cols]
df3.columns = [col+"_3" for col in origin_cols]
df4.columns = [col+"_4" for col in origin_cols]
df_join = df1.join([df2, df3, df4])
print(len(df_join))

df_join.to_csv("data/整合数据.csv")
