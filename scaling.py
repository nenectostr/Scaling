import numpy as np
import json
import os
from sklearn import preprocessing as skp
# наименовний
# порядковая
# интервальная
# отношений
# полярная


def get_data(file_name, file_path):
    with open(os.path.join(file_path,file_name), "r") as f:
        d = json.load(f)
    return d

def save_data(file_name, file_path, d):
    with open(os.path.join(file_path,file_name), "w") as f:
        json.dump(d, f)


def to_named(d):
    d["named"] = [str(i) for i in d[list(d.keys())[0]]]
    return d


def to_interval(d, int_amount=10):
    a = d[list(d.keys())[0]]
    ints = [i for i in np.arange(min(a), max(a), (max(a)-min(a))/int_amount)]
    intervals = [(int(round(ints[i])), int(round(ints[i+1]))) for i in range(len(ints)-1)]
    d["interval"] = []
    for i in a:
        for j in intervals:
            if j[0] < i < j[1]:
                d["interval"].append(j)
    return d


def to_ordered(d):
    a = d[list(d.keys())[0]]
    s = sorted(a)
    d["ordered"] = [s.index(i) for i in a]
    return d

def to_polar(d):
    a = d[list(d.keys())[0]]
    d["polar"] = []
    mean = np.mean(a)
    for i in a:
            if i > mean:
                d["polar"].append(1)
            else:
                d["polar"].append(-1)
    return d


def first_example():
    d = get_data("float_num.json", "data")
    # d = get_data("int_num.json", "data")
    # d = get_data("intervals.json", "data")
    # d = get_data("named.json", "data")
    # d = get_data("polar.json", "data")
    # d = get_data("ranks.json", "data")
    d = to_polar(d)
    for i in d:
        print(i + ":")
        print(d[i])
    save_data("saved_example.json", ".", d)


def second_example():
    d = get_data("named.json", "data")
    print("from")
    print(d)
    enc = skp.OneHotEncoder()
    a = np.array(d[list(d.keys())[0]]).reshape(-1, 1)
    enc.fit(a)
    arr = enc.transform(a).toarray()
    print("")
    print(arr)

if __name__ == '__main__':
    first_example()
    second_example()
