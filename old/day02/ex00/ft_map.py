#! /usr/bin/python3

def ft_map(function_to_apply, list_of_inputs):
    ret = []
    for i in list_of_inputs:
        ret.append(function_to_apply(i))
    return ret

print("Real function")
func = lambda x: x.upper()
test = (map(func, ['a', 'b']))
print(list(test))

print("My function")
func = lambda x: x.upper()
test = (ft_map(func, ['a', 'b']))
print(list(test))
