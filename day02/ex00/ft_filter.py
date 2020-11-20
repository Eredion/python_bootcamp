#! /usr/bin/python3

def ft_filter(function_to_apply, list_of_inputs):
    ret = []
    for i in list_of_inputs:
        if (function_to_apply(i)):
            ret.append(i)
    return ret

print("Real function")
func = lambda x: x.isupper()
test = (filter(func, ['A', 'b']))
print(list(test))

print("My function")
test = (ft_filter(func, ['A', 'b']))
print(list(test))
