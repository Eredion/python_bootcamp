#!/usr/bin/env python

#%%
import numpy as np
from matplotlib import pyplot as plt
import math


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

    def gradient(self, x, y):
        y_hat = self.predict_(x).reshape(np.size(y),)
        y = y.reshape(np.size(y),)
        X = self.add_intercept(x)
        X_t = np.transpose(X)
        return X_t @ (y_hat - y) / x.size

    def fit_(self, x, y):
        for i in range(self.max_iter):
            self.theta = self.theta - self.alpha * self.gradient(x, y)
        return self.theta

    def mse_(self, y, y_hat):
        return(np.dot((1 / (len(y)))*(y_hat - y), (y_hat - y)))


    def rmse_(self, y, y_hat):
        ret = self.mse_(y, y_hat)
        return (math.sqrt(ret))


    def mae_(self, y, y_hat):
        return(np.sum((abs((y_hat - y))/len(y))))


    def r2score_(self, y, y_hat):
        return 1.0 - (np.sum((y_hat - y) ** 2) / np.sum((y - np.mean(y)) ** 2))
    #%%


if __name__ == '__main__':

    csvData = np.genfromtxt('./are_blue_pills_magic.csv', delimiter=',')
    csvData = csvData.transpose()
    x = csvData[1][1:]
    y = csvData[2][1:]
#%%

    linear_model1 = MyLinearRegression(np.array([89.0, -8]))
    y_1 = linear_model1.predict_(x)
    print(y_1)
    theta = linear_model1.fit_(x, y)
    y_1 = linear_model1.predict_(x)
    print(y_1)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, 'o')
    for i in range(0, len(y)):
            ax.plot([x[i], x[i]], [y[i], y_1[i]],
                    linestyle='--', color='red')
            ax.plot(x, theta[1] * x + theta[0], linestyle="--", color='green')
    plt.show()

# %%
