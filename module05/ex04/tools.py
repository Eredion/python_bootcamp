#!/usr/bin/env python

import numpy as np

def add_intercept(x):
    """
    Adds a column of ones to the left of the matrix x.
    Args:
        x: has to be an numpy.ndarray, a vector of dimension m * 1.
    Returns:
        has to be an numpy.ndarray, a vector of dimension m * 2.
        None if x is not a numpy.ndarray.
        None if x does not have the right dimensions.
    Raises:
        This function should not raise any Exception.
    """

    if type(x) != np.ndarray or np.size(x) == 0:
        return None
    if x.ndim == 1:
        x = x.reshape(np.size(x), 1)
    return np.hstack((np.ones((x.shape[0], 1)), x))


if __name__ == "__main__":
    print(add_intercept(np.arange(1,6)))
    print(add_intercept(np.arange(1,10).reshape(3,3)))
