import pandas as pd
import matplotlib.pyplot as plt
import csv


def merge_log(df1, df2):
    data = df1.join(df2, how="outer")
    return data


def parse_log():
    data = pd.DataFrame(columns=['time', 'log', 'message'])
    file = open("ssrlcv.log")
    for line in file:
        temp = line.split(',')
        time = temp[0]
        log = temp[1]
        message = ", ".join(temp[2:]).replace('\n', '').strip()
        data = data.append(
            other={
                'time': int(time),
                'log': log,
                'message': message
            },
            ignore_index=True
        )
    data.set_index(keys=data.time, inplace=True)
    data.drop(columns='time', inplace=True)
    return data


def parse_memory():
    data = pd.read_csv("memory.csv")
    data.drop(columns=['total', 'host_unpinned', 'host_pinned', 'device'], inplace=True)
    data.rename(
        columns={
            data.columns[0]: 'time',
            data.columns[1]: 'total',
            data.columns[2]: 'host_unpinned',
            data.columns[3]: 'host_pinned',
            data.columns[4]: 'device'
        },
        inplace=True
    )
    data.set_index(keys=data.time, inplace=True)
    data.drop(columns='time', inplace=True)
    return data


if __name__ == "__main__":
    mem = parse_memory()
    log = parse_log()
    dt = merge_log(mem, log)
    dt.sort_index(inplace=True)
    dt.to_csv("data.csv")
