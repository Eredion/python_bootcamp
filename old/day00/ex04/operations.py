#! /usr/bin/python3

import sys
from termcolor import colored

def usage():
    print(colored('Usage:', 'blue'), "python operations.py <number1> <number2>")
    print(colored('Example:', 'blue'), "\n\t python operations.py 10 3")
    return

if len(sys.argv) == 1:
    usage()
elif len(sys.argv) == 2:
    print(colored('InputError:', 'blue'), "not enough arguments\n")
    usage()
elif len(sys.argv) > 3:
    print(colored('InputError:', 'blue'), "too many arguments\n")
    usage()
elif sys.argv[1].isnumeric() == False | sys.argv[2].isnumeric() == False:
    print(colored('InputError:', 'blue'), "only numbers\n")
    usage()
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(colored('Sum:', 'blue'), "\t\t", (a + b))
    print(colored('Difference:', 'blue'), "\t", (a - b))
    print(colored('Product:', 'blue'), "\t", (a * b))
    if b == 0:
        print(colored('Quotient:', 'blue'), "\t ERROR (div by zero)")
        print(colored('Reminder:', 'blue'), "\t ERROR (modulo by zero)")
    else:
        print(colored('Quotient:', 'blue'), "\t", (a / b))
        print(colored('Reminder:', 'blue'), "\t", (a % b))
