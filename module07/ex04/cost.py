#!/usr/bin/env python

import numpy as np

def cost_(y, y_hat):
    return np.mean((y - y_hat) ** 2)/2

if __name__ == '__main__':
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    print(cost_(X, Y))
    print(cost_(X, X))
