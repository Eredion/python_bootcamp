#! /usr/bin/python3

import numpy

class NumPyCreator():
    @staticmethod
    def from_list(lst):
        return numpy.array(lst)
    
    @staticmethod
    def from_tuple(tpl):
        return numpy.array(tpl)
    
    @staticmethod
    def from_iterable(itr):
        return numpy.array(itr)

    @staticmethod
    def from_shape(shape, value):
        return numpy.full(shape, value)

if __name__ == "__main__":

    num = NumPyCreator()

    print(str(num.from_list([[1,2],[3,4]])))

    print(str(num.from_list((1,2))))

