#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict(x, theta):
    if np.ndim(x) != 1 or np.ndim(theta) != 1 or theta.size != 2 or x.size == 0:
        return None
    return add_intercept(x) @ theta

if __name__ == "__main__":
    print(predict(np.arange(1,6), np.array([5, 0])))
    print(predict(np.arange(1,6), np.array([0, 1])))
    print(predict(np.arange(1,6), np.array([5, 3])))
    print(predict(np.arange(1,6), np.array([-3, 1])))


