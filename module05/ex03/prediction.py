#!/usr/bin/env python

import numpy as np

def simple_predict(x, theta):
    """"
    Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
        theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
        y_hat as a numpy.ndarray, a vector of dimension m * 1.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
    Raises:
        This function should not raise any Exception.
    """
    if np.ndim(x) != 1 or np.ndim(theta) != 1 or theta.size != 2 or x.size == 0:
        return None
    return x * theta[1] + theta[0]


if __name__ == "__main__":
    print(simple_predict(np.arange(1,6), np.array([5, 0])))
    print(simple_predict(np.arange(1,6), np.array([0, 1])))
    print(simple_predict(np.arange(1,6), np.array([5, 3])))
    print(simple_predict(np.arange(1,6), np.array([-3, 1])))

