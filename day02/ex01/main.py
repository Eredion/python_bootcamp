#! /usr/bin/python3

import sys

def what_are_the_vars(*args, **kwargs):
    ret = ObjectC()
    for i in range(len(args)):
       setattr(ret, "var_{}".format(str(i)), args[i])
    for k, v in kwargs.items():
       if k in dir(ret):
            return
       setattr(ret, k, v)
    return ret

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0,0,0], a=10, hello='wordl')
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="wordl")
    doom_printer(obj)
