#!/usr/bin/env python

import sys

def calcs(x, y):
    """
    This functions takes two numbes and return the basic operations.
    """
    print('Sum:        ', x + y)
    print('Difference: ', x - y)
    print('Product:    ', x * y)

    if y != 0:
        print('Quotient:   ', x / y)
        print('Remainder:  ', x % y)
    else:
        print('Quotient:    ERROR (div by zero)')
        print('Remainder:   ERROR (modulo by zero)')

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise ValueError("ERROR")
        calcs(int(sys.argv[1]), int(sys.argv[2]))
    except ValueError:
            print ("ERROR")
