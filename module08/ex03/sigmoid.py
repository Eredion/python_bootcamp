#!/usr/bin/env python

import numpy as np

def sigmoid_(x):
    """
    Compute the sigmoid of a vector.
    Args:
        x: has to be a numpy.ndarray, a vector.
    Returns:
        The sigmoid value as a numpy.ndarray.
        None if x is an empty numpy.ndarray.
    Raises:
        This function should not raise any Exception.
    """
    if x.size == 0:
        return None
    if type(x) != np.ndarray:
        return None
    return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
    x = np.array([-4])
    print(sigmoid_(x))

    x = np.array([[-4], [2], [0]])
    print(sigmoid_(x))

