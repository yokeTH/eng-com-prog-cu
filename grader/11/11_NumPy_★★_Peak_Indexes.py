import numpy as np


def peak_indexes(x):
    d = np.diff(np.sign(np.diff(x)))
    indexs = np.arange(1, len(x)-1)
    return indexs[d < -1]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())