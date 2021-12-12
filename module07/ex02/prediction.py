#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))

def simple_predict(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a matrix of dimension m * n.
      theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not matching.
      None if x or theta are not of the expected type objects.
    Raises:
      This function should not raise any Exception.
    """
    if type(x) is not np.ndarray or type(theta) is not np.ndarray:
        return None
    if x.size == 0 or theta.size == 0:
        return None
    theta = theta.reshape(theta.size, 1)
    x = add_intercept(x)
    return np.dot(x, theta)


if __name__ == "__main__":
    x = np.arange(1,13).reshape((4,-1))
    theta1 = np.array([5, 0, 0, 0])
    print(simple_predict(x, theta1))

    theta2 = np.array([0, 1, 0, 0])
    print(simple_predict(x, theta2))

    theta3 = np.array([-1.5, 0.6, 2.3, 1.98])
    print(simple_predict(x, theta3))

    theta4 = np.array([-3, 1, 2, 3.5])
    print(simple_predict(x, theta4))
