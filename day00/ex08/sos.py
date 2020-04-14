import sys

def check(args):
    for i in args:
        for j in i:
            if j != '.' and j != '-' and j != '/':
                return (0)

Morse_code  = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-', ' ' : '/'}
Morse_code = {v: k for k, v in Morse_code.items()}

if __name__ == "__main__":
    if len(sys.argv) < 2 or check(sys.argv[1::]) == 0:
        print("ERROR")
        exit(1)
    try:
        for i in sys.argv[1:]:
            print(Morse_code[i], end="")
    except KeyError:
        print('ERROR')
        exit(1)
    print()
    exit()
