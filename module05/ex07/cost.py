#!/usr/bin/env

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict_(x, theta):
    if np.ndim(x) != 1 or np.ndim(theta) != 1 or theta.size != 2 or x.size == 0:
        return None
    return add_intercept(x) @ theta

def cost_elem_(y, y_hat):
    return (y_hat - y) ** 2

def cost_(y, y_hat):
    return np.sum(cost_elem_(y, y_hat)) / y.size




if __name__ == "__main__":
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    print("hola")
    y_hat1 = predict_(x1, theta1)
    print(y_hat1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    print(cost_elem_(y1, y_hat1))
    print(cost_(y1, y_hat1))

    x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    theta2 = np.array([[0.05], [1.], [1.], [1.]])
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([[19.], [42.], [67.], [93.]])
    print(cost_elem_(y2, y_hat2))
    print(cost_(y2, y_hat2))

    x3 = np.array([0, 15, -9, 7, 12, 3, -21])
    theta3 = np.array([[0.], [1.]])
    y_hat3 = predict_(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19])

    print(cost_(y3, y_hat3))
    print(cost_(y3, y3))
