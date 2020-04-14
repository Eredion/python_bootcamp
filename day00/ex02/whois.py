import sys

if len(sys.argv) == 1:
    exit()
if len(sys.argv) > 2 or sys.argv[1].isdigit() == 0 :
    print("ERROR")
    exit()
i = int(sys.argv[1])
if i == 0:
    print("I'm Zero.")
elif i % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
