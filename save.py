import csv
import os
from datetime import datetime


data_path = 'data.csv'
# if not os.path.exists(data_path):


def load():
    state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
    if not os.path.exists(data_path):
        return state, 1
    with open(data_path, 'r') as data:
        reader = list(csv.reader(data))
        i = 0
        for row in reader:
            i += 1
            print(row[0], row[2])

        if i < 2:
            return state, 1
        game_num = int(input("enter game number to be loaded: "))
        for j, row in enumerate(reader):
            if j == game_num:
                return [int(x) for x in row[1].split()], int(row[-1])


def save(state, stealing):
    with open(data_path, 'r+') as data:
        writer = csv.writer(data)
        reader = list(csv.reader(data))
        ln = len(reader)

        if os.stat(data_path).st_size == 0:
            ln += 1
            writer.writerow(["index", "state", "time"])

        s = ""
        for i in state:
            s = s + str(i) + " "
        s = s.strip()
        writer.writerow([ln, s, datetime.now(), stealing])

    return True


def clear_data():
    f = open(data_path, "w")
    f.truncate()
    f.close()


if __name__ == "__main__":
    clear_data()
