#!/usr/bin/env python

#%%

import numpy as np
import matplotlib.pyplot as plt

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

def plot(x, y, theta):
    """
    Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        y: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        Nothing.
    Raises:
        This function should not raise any Exception.
    """
    if type(x) != np.ndarray or x.ndim != 1 or x.size == 0:
        return None
    if type(y) != np.ndarray or y.ndim != 1 or y.size == 0:
        return None
    if type(theta) != np.ndarray or theta.ndim != 1 or theta.size != 2:
        return None
    plt.plot(x, y, 'r*')
    plt.plot(x, predict(x, theta))
    #plt.xlabel('x')
    #plt.ylabel('y')
    plt.show()

if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([3.74, 3.61, 4.57, 4.67, 5.955])
    plot(x, y, np.array([4.5, -0.2]))

# %%
