import sys

out = ''
for i in (sys.argv[1: ]):
    out = out + ' ' + i.swapcase()

out = out[1: ]
print (out[::-1])
