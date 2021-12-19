#!/usr/bin/env python

import numpy as np

def logistic_predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
      x: has to be an numpy.ndarray, a vector of dimension m * n.
      theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
      y_hat as a numpy.ndarray, a vector of dimension m * 1.
      None if x or theta are empty numpy.ndarray.
      None if x or theta dimensions are not appropriate.
    Raises:
      This function should not raise any Exception.
    """
    if x.size == 0 or theta.size == 0:
        return None
    if type(x) != np.ndarray or type(theta) != np.ndarray:
        return None
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    x = np.insert(x, 0, 1, axis=1)
    return 1 / (1 + np.exp(-(np.dot(x, theta))))

if __name__ == '__main__':
    x = np.array([4])
    theta = np.array([[2], [0.5]])
    print(logistic_predict_(x, theta))

    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])
    print(logistic_predict_(x2, theta2))
