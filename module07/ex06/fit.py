#!/usr/bin/env python

import numpy as np

def cost_(y, y_hat):
    y = y.reshape(np.size(y),)
    y_hat = y_hat.reshape(np.size(y_hat),)
    return np.mean((y - y_hat) ** 2)/2

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict_(x, theta):
    if type(x) is not np.ndarray or type(theta) is not np.ndarray:
        return None
    if x.size == 0 or theta.size == 0:
        return None
    theta = theta.reshape(theta.size, 1)
    x = add_intercept(x)
    return (x @ theta)

def gradient(x, y, theta):
    y_hat = predict_(x, theta).reshape(np.size(y),)
    y = y.reshape(np.size(y),)
    X = add_intercept(x)
    X_t = np.transpose(X)
    return X_t @ (y_hat - y) / x.size


def fit_(x, y, theta, alpha = 0.0005, max_iter = 4200):
    theta = theta.reshape(theta.size, 1)
    for i in range(max_iter):
        theta = theta - alpha * gradient(x, y, theta).reshape(theta.size, 1)
    return theta


if __name__ == '__main__':
    x = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8., 80.]])
    y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
    theta = np.array([[42.], [1.], [1.], [1.]])


    theta2 = fit_(x, y, theta,  alpha = 0.0005, max_iter=42000)
    print(theta2)

    print(predict_(x, theta2))
