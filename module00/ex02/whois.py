#!/usr/bin/env python

import sys

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("ERROR")
        n = int(sys.argv[1])
        if n == 0:
            print("I'm Zero.")
        elif n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")
        sys.exit(1)

if __name__ == "__main__":
    main()
