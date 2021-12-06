#!/usr/bin/env python

import numpy as np

def minmax(x):
    min = np.min(x)
    div = np.max(x) - min
    return (x - min) / div

if __name__ == '__main__':
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    print(minmax(X))

    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    print(minmax(Y))

