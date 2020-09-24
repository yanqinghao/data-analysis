import os
import pandas as pd

if __name__ == '__main__':
    files = []
    for (dirpath, dirnames, filenames) in os.walk("data/csvs"):
        filelist = [os.path.join(dirpath, filename) for filename in filenames]
        files.extend(filelist)
    # files = ["data/project/2018.4/#20_3串20184992813.txt"]
    dfs = []
    for file in files:
        if "4串" in file:
            df = pd.read_csv(file, index_col=0)
            time = list(df.columns)[0]
            df = df[df[time].str.contains("[0-9]{4}", regex=True, na=False)]
            df[time] = pd.to_datetime(df[time], errors='coerce').dt.strftime("%Y-%m-%d %H:%M:%S")
            if list(df.columns) == [
                    '时间', '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib',
                    'Uc', 'Ic', 'Pac', 'cosφ', 'Qpy', 'Qdc', 'Qac', 'Eff '
            ]:
                dfs.append(df)
            else:
                df.columns = [
                    '时间', '辐照度', '环境温度', 'Udc', 'Idc', 'Pdc', 'Ua', 'Ia', 'Ub', 'Ib',
                    'Uc', 'Ic', 'Pac', 'cosφ', 'Qpy', 'Qdc', 'Qac', 'Eff '
                ]
                dfs.append(df)

    df_merged = pd.concat(dfs)
    df_merged.sort_values(by="时间", inplace=True)
    df_merged.reset_index(inplace=True, drop=True)
    df_merged.to_csv("data/4串.csv")
