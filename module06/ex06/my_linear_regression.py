#!/usr/bin/env python

import numpy as np

class MyLinearRegression:
    """
    Description:
        My personnal linear regression class to fit like a boss.
    """
    def __init__(self, theta, alpha=0.001, max_iter=1000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = np.array(theta)

    def cost_elem_(y, y_hat):
        y = y.reshape(np.size(y),)
        y_hat = y_hat.reshape(np.size(y_hat),)
        return (y_hat - y) ** 2

    def cost_(y, y_hat):
        y = y.reshape(np.size(y),)
        y_hat = y_hat.reshape(np.size(y_hat),)
        return np.dot(y_hat - y, y_hat - y) / len(y) * 0.5

    def add_intercept(self, x):
        if type(x) != np.ndarray or np.size(x) == 0:
            return None
        if x.ndim == 1:
            x = x.reshape(np.size(x), 1)
        return np.hstack((np.ones((x.shape[0], 1)), x))

    def predict_(self, x):
        if  self.theta.size != 2 or x.size == 0:
            return None
        return self.add_intercept(x) @ self.theta

    def gradient(self, x, y, theta):
        y_hat = self.predict_(x).reshape(np.size(y),)
        y = y.reshape(np.size(y),)
        X = self.add_intercept(x)
        X_t = np.transpose(X)
        return X_t @ (y_hat - y) / x.size

    def fit_(self, x, y):
        for i in range(self.max_iter):
            self.theta = self.theta - self.alpha * self.gradient(x, y, self.theta)
        return self.theta

if __name__ == '__main__':
    x = np.array([[12.4956442], [21.5007972], [31.5527382], [48.9145838], [57.5088733]])
    y = np.array([[37.4013816], [36.1473236], [45.7655287], [46.6793434], [59.5585554]])

    lr1 = MyLinearRegression([2, 0.7])

    print(lr1.predict_(x))

    print(MyLinearRegression.cost_elem_(y, lr1.predict_(x)))

    print(MyLinearRegression.cost_(y, lr1.predict_(x)))

    lr2 = MyLinearRegression([1, 1], 5e-8, 1500000)
    print(lr2.fit_(x, y))
    print(lr2.predict_(x))

    print(MyLinearRegression.cost_elem_(y, lr2.predict_(x)))

    print(MyLinearRegression.cost_(y, lr2.predict_(x)))
