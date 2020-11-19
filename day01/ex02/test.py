#! /usr/bin/env python3

from vector import Vector

a = Vector(3)
b = Vector(3, 6)
print(a)
print(repr(b))

print('Testing sum')
c = a + b
print(c)
print("c + 3.5 = "+ str(c + 3.5))
print("6.3 + c = "+ str(6.3 + c))

print('Testing susbstraction')
c = a - b
print(c)
print("c - 3.5 = "+ str(c - 3.5))
print("6.3 - c = "+ str(6.3 - c))

print('Testing multiplication')
c = a * b
print(c)
print("[0.5, 3] * 3.5 = "+ str(Vector([0.5, 3.5]) * 3.5))
print("6.3 * [0.5, 3] = "+ str(6.3 * Vector([0.5, 3.5])))

