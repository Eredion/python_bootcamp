#!/usr/bin/env python

from functools import reduce

def ft_map(function_to_aply, list_of_inputs):
    for i in list_of_inputs:
        yield function_to_aply(i)


def ft_filter(function_to_aply, list_of_inputs):
    for i in list_of_inputs:
        if function_to_aply(i):
            yield i

def ft_reduce(function_to_aply, list_of_inputs):
    ret = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        ret = function_to_aply(ret, i)
    return ret

def sum1(x):
    return x + 1

def isOdd(x):
    return x % 2 == 1

if __name__ == "__main__":

    print("\nMy map")
    for i in ft_map(sum1, [1, 2, 3, 4, 5]):
        print(i, end=" ")
    print("\nReal map")
    for i in map(sum1, [1, 2, 3, 4, 5]):
        print(i, end=" ")

    print("\nMy filter")
    for i in ft_filter(isOdd, [1, 2, 3, 4, 5]):
        print(i, end=" ")
    print("\nReal filter")
    for i in filter(isOdd, [1, 2, 3, 4, 5]):
        print(i, end=" ")

    print("\nMy reduce")
    print(ft_reduce((lambda x,y: x+y), [1, 2, 3, 4, 5]))
    print("Real reduce")
    print(reduce((lambda x,y: x+y), [1, 2, 3, 4, 5]))
