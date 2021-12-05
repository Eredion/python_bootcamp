#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def predict(x, theta):
    if  theta.size != 2 or x.size == 0:
        return None
    return add_intercept(x) @ theta

def simple_gradient(x, y, theta):
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
    y_hat = predict(x, theta)
    ret = [0, 0]
    ret[0] = (y_hat - y).sum() / x.size
    ret[1] = ((y_hat - y) * x).sum() / x.size
    return np.array(ret)


if __name__ == "__main__":

    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733])
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554])

    theta1 = np.array([2, 0.7])
    print(simple_gradient(x, y, theta1))

    theta2 = np.array([1, -0.4])
    print(simple_gradient(x, y, theta2))
