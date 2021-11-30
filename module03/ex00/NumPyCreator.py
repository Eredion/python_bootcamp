#!/usr/bin/env python

import numpy as np

class NumPyCreator:
    def from_list(lst):
        return np.array(lst)

    def from_tuple(tpl):
        return np.array(tpl)

    def from_range(range):
        return np.array(range)

    def from_shape(shape):
        return np.zeros(shape)

    def random(shape):
        return np.random.random(shape)

    def identity(n):
        return np.identity(n)
