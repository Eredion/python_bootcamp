#! /usr/bin/python3

import functools

def ft_reduce(function_to_apply, list_of_inputs):
    ret = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        ret = function_to_apply(ret, i)
    return ret

sum = lambda x, y: x + y
s = [1,2,3,4]

print("Input = sum of "+ str(s))

print("My reduce")
a = ft_reduce(sum, s)
print(a)

print("Real reduce")
a = functools.reduce(sum, s)
print(a)
