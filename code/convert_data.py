import os
import codecs
import csv
import pandas as pd


def txt_reader(path):
    data = []
    with codecs.open(path, encoding="GBK", errors="ignore") as txt_file:
        txt_reader = csv.reader([x.replace('\0', '') for x in txt_file], delimiter="\t")
        line = 0
        for row in txt_reader:
            if len(row) == 1 and line == 0:
                if len(row[0].split("   ")) > 1:
                    data.append(row[0].split("   ")[1:])
                else:
                    data.append(row[0].split(" , ")[1:])
                line += 1
            else:
                if len(row) == 1:
                    data.append(row[0].split(",")[:18])
                else:
                    data.append(row[:18])
    df = pd.DataFrame(data[1:], columns=data[0])
    return df


if __name__ == '__main__':
    files = []
    for (dirpath, dirnames, filenames) in os.walk("data/project"):
        filelist = [os.path.join(dirpath, filename) for filename in filenames]
        files.extend(filelist)
    # files = ["data/project/2018.4/#20_3串20184992813.txt"]
    for file in files:
        df = txt_reader(file)
        paths = file.split("/")
        paths[1] = "csvs"
        paths[-1] = paths[-1].replace(".txt", ".csv")
        export_path = os.path.join(*paths)
        os.makedirs(os.path.join(*paths[:-1]), exist_ok=True)
        df.to_csv(export_path)
