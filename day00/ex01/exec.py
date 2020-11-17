#!/usr/bin/python3.8

import sys

str = ''
for x in sys.argv[1:]:
    str += x

str_rev = str[::-1]
print(str_rev.swapcase())
