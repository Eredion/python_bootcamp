#!/usr/bin/env python

import numpy as np
from log_pred import logistic_predict_

def vec_log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The three arrays must have compatible shapes.
    Args:
      x: has to be an numpy.ndarray, a matrix of shape m * n.
      y: has to be an numpy.ndarray, a vector of shape m * 1.
      theta: has to be an numpy.ndarray, a vector (n +1) * 1.
    Returns:
      The gradient as a numpy.ndarray, a vector of shape n * 1, containg the result of the formula for all j.
      None if x, y, or theta are empty numpy.ndarray.
      None if x, y and theta do not have compatible shapes.
    Raises:
      This function should not raise any Exception.
    """
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    if type(x) != np.ndarray or type(y) != np.ndarray or type(theta) != np.ndarray:
        return None
    if x.ndim == 1:
        x = x.reshape(x.shape[0], 1)
    if y.ndim == 1:
        y = y.reshape(y.shape[0], 1)
    if theta.ndim == 1:
        theta = theta.reshape(theta.shape[0], 1)
    if x.shape[1] != theta.shape[0] - 1 or x.shape[0] != y.shape[0] or y.shape[1] != 1:
        return None

    y_hat = logistic_predict_(x, theta)
    return  np.insert(x, 0, 1, axis=1).transpose() @ (y_hat - y) / y.shape[0]


if __name__ == '__main__':

    y1 = np.array([1])
    x1 = np.array([4])
    theta1 = np.array([[2], [0.5]])

    print(vec_log_gradient(x1, y1, theta1))

    y2 = np.array([[1], [0], [1], [0], [1]])
    x2 = np.array([[4], [7.16], [3.2], [9.37], [0.56]])
    theta2 = np.array([[2], [0.5]])

    print(vec_log_gradient(x2, y2, theta2))

    y3 = np.array([[0], [1], [1]])
    x3 = np.array([[0, 2, 3, 4], [2, 4, 5, 5], [1, 3, 2, 7]])
    theta3 = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])

    print(vec_log_gradient(x3, y3, theta3))
