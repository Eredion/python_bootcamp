#! /usr/bin/python3.8

import sys

str = "buenos dias"

c = 0;

for i in sys.argv:
    c += 1

if c != 2:
    print("ERROR")
    exit()
try:
    c = int(sys.argv[1])
except:
    exit("ERROR")
if c == 0:
    print("I'm Zero.")
elif (c % 2 == 0):
    print("I'm Even.")
elif (c % 2 == 1):
    print("I'm Even.")
