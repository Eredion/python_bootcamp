#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
import math


class MyLinearRegression:
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, theta, alpha=0.0001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = np.array(theta)

    def cost_elem_(self, x, y):
        y_hat = self.predict_(x)
        return (y_hat - y) ** 2

    def cost_(self, x, y):
        y = y.reshape(np.size(y), 1)
        y_hat = self.predict_(x)
        return np.mean((y - y_hat) ** 2)/2

    def add_intercept(self, x):
        if type(x) != np.ndarray or np.size(x) == 0:
            return None
        if x.ndim == 1:
            x = x.reshape(np.size(x), 1)
        return np.hstack((np.ones((x.shape[0], 1)), x))

    def predict_(self, x):
        if type(x) is not np.ndarray or type(self.theta) is not np.ndarray:
            return None
        if x.size == 0 or self.theta.size == 0:
            return None
        self.theta = self.theta.reshape(self.theta.size, 1)
        x = self.add_intercept(x)
        return (x @ self.theta)

    def gradient(self, x, y):
        y_hat = self.predict_(x).reshape(np.size(y),)
        y = y.reshape(np.size(y),)
        X = self.add_intercept(x)
        X_t = np.transpose(X)
        return X_t @ (y_hat - y) / x.size

    def fit_(self, x, y):
        self.theta = self.theta.reshape(self.theta.size, 1)
        for i in range(self.max_iter):
            self.theta = self.theta - self.alpha * self.gradient(x, y).reshape(self.theta.size, 1)

    def mse_(self, y, y_hat):
        return(np.dot((1 / (len(y)))*(y_hat - y), (y_hat - y)))


    def rmse_(self, y, y_hat):
        ret = self.mse_(y, y_hat)
        return (math.sqrt(ret))


    def mae_(self, y, y_hat):
        return(np.sum((abs((y_hat - y))/len(y))))


    def r2score_(self, y, y_hat):
        return 1.0 - (np.sum((y_hat - y) ** 2) / np.sum((y - np.mean(y)) ** 2))


if __name__ == '__main__':

    X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89., 144.]])
    Y = np.array([[23.], [48.], [218.]])
    mylr = MyLinearRegression([[1.], [1.], [1.], [1.], [1]])

    print(mylr.predict_(X))

    print(mylr.cost_elem_(X,Y))

    print(mylr.cost_(X,Y))

    mylr.alpha = 1e-4
    mylr.max_iter = 2000000
    mylr.fit_(X, Y)
    print(mylr.theta)

    print(mylr.predict_(X))

    print(mylr.cost_elem_(X,Y))

    print(mylr.cost_(X,Y))
