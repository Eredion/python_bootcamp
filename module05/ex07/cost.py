#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict_(x, theta):
    if theta.size != 2 or x.size == 0:
        return None
    return add_intercept(x) @ theta

def cost_elem_(y, y_hat):
    return (y_hat - y) ** 2

def cost_(y, y_hat):
    return np.sum(cost_elem_(y, y_hat)) / (y.size * 2)




if __name__ == "__main__":
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    print(cost_elem_(y1, y_hat1))
    print(cost_(y1, y_hat1))

    x3 = np.array([0, 15, -9, 7, 12, 3, -21])
    theta3 = np.array([[0.], [1.]])
    y_hat3 = predict_(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19])

    print(cost_(y3, y_hat3))
    print(cost_(y3, y3))

