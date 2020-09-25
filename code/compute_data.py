import pandas as pd
import numpy as np

df = pd.read_csv("data/整合数据.csv")
time_formats = ["%Y-%m-%d", "%Y-%m", "%Y"]
titles = ["日", "月", "年"]
for time_format, title in zip(time_formats, titles):
    df_analysis = df[[
        "time_new", "辐照度", "辐照度_2", "辐照度_3", "辐照度_4", "环境温度", "环境温度_2", "环境温度_3", "环境温度_4", "Pdc",
        "Pdc_2", "Pdc_3", "Pdc_4", "Pac", "Pac_2", "Pac_3", "Pac_4", "Eff ", "Eff _2", "Eff _3",
        "Eff _4"
    ]]
    time = "time_new"
    df_analysis[title] = pd.to_datetime(df[time]).dt.strftime(time_format)
    df_analysis.drop(time, axis=1, inplace=True)
    df_analysis = df_analysis.replace([np.inf, -np.inf], np.nan)
    df_grouped1 = df_analysis.groupby(title)["Eff ", "Eff _2", "Eff _3", "Eff _4", "环境温度"].mean()
    df_grouped1.columns = ["Eff_1", "Eff_2", "Eff_3", "Eff_4", "temp"]
    df_grouped2 = df_analysis.groupby(title)["辐照度", "Pdc", "Pdc_2", "Pdc_3", "Pdc_4", "Pac",
                                             "Pac_2", "Pac_3", "Pdc_4"].sum() / 60
    df_grouped2.columns = [
        "irr", "Pdc_1_sum", "Pdc_2_sum", "Pdc_3_sum", "Pdc_4_sum", "Pac_1_sum", "Pac_2_sum",
        "Pac_3_sum", "Pdc_4_sum"
    ]
    df_grouped = df_grouped1.join(df_grouped2)
    df_grouped.to_csv("data/每" + title + "统计.csv")
