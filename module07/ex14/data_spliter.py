#!/usr/bin/env python

import numpy as np

def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a training and a test set, while respecting the given proportion of examples to be kept in the traning set.
    Args:
      x: has to be an numpy.ndarray, a matrix of dimension m * n.
      y: has to be an numpy.ndarray, a vector of dimension m * 1.
      proportion: has to be a float, the proportion of the dataset that will be assigned to the training set.
    Returns:
      (x_train, x_test, y_train, y_test) as a tuple of numpy.ndarray
      None if x or y is an empty numpy.ndarray.
      None if x and y do not share compatible dimensions.
    Raises:
      This function should not raise any Exception.
    """
    if type(proportion) != float or type(x) != np.ndarray or y.ndim != 1\
        or len(y) == 0 or type(y) != np.ndarray or x.shape[0] != y.shape[0]:
        return None
    if x.ndim == 1:
        X = np.concatenate((y.reshape(len(y), 1), x.reshape(len(x), 1)),
            axis=1)
    else:
         X = np.concatenate((y.reshape(len(y), 1), x), axis=1)

    X = np.random.permutation(X)
    prop = int(proportion * len(y))
    train =(X[:prop,:])
    test = (X[prop:,:])
    ret_train = np.hsplit(train, np.array([1, len(y)]))
    ret_test = np.hsplit(test, np.array([1, len(y)]))
    return ret_train[1].transpose(), ret_test[1].transpose(),\
        ret_train[0].transpose(), ret_test[0].transpose()

if __name__ == '__main__':
    x1 = np.array([1, 42, 300, 10, 59])
    y = np.array([0, 1, 0, 1, 0])

    print(data_spliter(x1, y, 0.8))
    print(data_spliter(x1, y, 0.5))

    x2 = np.array([[  1, 42],
                   [300, 10],
                   [ 59,  1],
                   [300, 59],
                   [ 10, 42]])
    y = np.array([0, 1, 0, 1, 0])

    print(data_spliter(x2, y, 0.8))
    print(data_spliter(x2, y, 0.5))
