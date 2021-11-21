#!/usr/bin/env python

import sys

str = ""

for i in sys.argv[1:][::-1]:
    str += i[::-1].swapcase() + " "

print(str[:-1])
