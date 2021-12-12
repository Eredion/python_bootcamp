#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict(x, theta):
    if type(x) is not np.ndarray or type(theta) is not np.ndarray:
        return None
    if x.size == 0 or theta.size == 0:
        return None
    theta = theta.reshape(theta.size, 1)
    x = add_intercept(x)
    return np.dot(x, theta)

def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The three arrays must have compatible dimensions.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * 1.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      theta: has to be an numpy.ndarray, a 2 * 1 vector.
    Returns:
      The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    y_hat = predict(x, theta).reshape(np.size(y),)
    print(y_hat)
    y = y.reshape(np.size(y),)
    X = add_intercept(x)
    X_t = np.transpose(X)
    return X_t @ (y_hat - y) / x.size


if __name__ == "__main__":

    x = np.array([
    	      [ -6,  -7,  -9],
            [ 13,  -2,  14],
            [ -7,  14,  -1],
            [ -8,  -4,   6],
            [ -5,  -9,   6],
            [  1,  -5,  11],
            [  9, -11,   8]])
    y = np.array([2, 14, -13, 5, 12, 4, -19])
    theta1 = np.array([0,3,0.5,-6])

    print(gradient(x, y, theta1))

    theta2 = np.array([0,0,0,0])
    print(gradient(x, y, theta2))

