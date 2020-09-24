import pandas as pd

df = pd.read_csv("data/1串.csv", index_col=0)

df["time_new"] = pd.to_datetime(df["时间"]).dt.strftime("%Y-%m-%d %H:%M")

df.drop("时间", axis=1, inplace=True)
df_grouped = df.groupby("time_new").mean()

df_grouped.to_csv("data/1组串_min.csv")
