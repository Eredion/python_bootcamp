import sys

def print_error():
    print("\033[1;34mInputError\033[0;0m", end = '')
    print(": only two numbers\n")
    print("\033[1;34mUsage\033[0;0m:", end = '')
    print(" python operations.ppy <number1> <number 2>")
    print("\033[1;34mExample\033[0;0m:", "\n    ", end = '')
    print("\033[1;34mpython\033[0;0m", "operations.py 10 3")
    exit()

def operations(args):
    """Do the basic operations to two given numbers"""
    if len(sys.argv) != 3 or args[1].isnumeric is False\
        or args[2].isnumeric is False:
        print_error()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("\033[1;34mSum\033[0;0m", end = '')
    print(":       ", a + b)
    print("\033[1;34mDifference\033[0;0m", end = '')
    print(":", a - b)
    print("\033[1;34mProduct\033[0;0m", end = '')
    print(":   ", a * b)
    if a == 0 or b == 0:
        print("\033[1;34mQuotient\033[0;0m", end = '')
        print(":   Error (div by zero)")
        print("\033[1;34mRemainder\033[0;0m", end = '')
        print(":  Error (modulo by zero)")
    else :
        print("\033[1;34mQuotient\033[0;0m", end = '')
        print(":  ", a / b)
        print("\033[1;34mRemainder\033[0;0m", end = '')
        print(": ", a % b)

operations(sys.argv)
