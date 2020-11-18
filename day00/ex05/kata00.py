#! /usr/bin/python3

t = (19,42,21)

print("The 3 numbers are:", format(t).replace('(','').replace(')','').replace('%n,','%n, ', 2))
