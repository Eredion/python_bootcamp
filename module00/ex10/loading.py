#!/usr/bin/env python

import sys
import time

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        eta = (j - count) * 0.1
        ela = j * 0.1
        percent = int(100*j/count)
        file.write("ETA: {}s [{}%][{}>{}] {}/{} | elapsed time {}s\r".format(eta.__round__(2), percent, "="*x, " "*(size - x), j, count,  ela.__round__(2)))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

if __name__ == "__main__":

    lst = range(1000)
    ret = 0
    for i in progressbar(lst):
        time.sleep(0.01) # any calculation you need
    print()
    print(ret)
