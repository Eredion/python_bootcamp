#! /usr/bin/python3

import sys

Morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',\
         'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',\
         'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',\
         'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',\
         'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',\
         '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',\
         '9':'----.', '0':'-----', ' ':'/'}

def morse_translator(word):
    msg = ''
    for i in word:
        msg += Morse[i.upper()] + ' '
    return msg

final_text = ''

try:
    for arg in sys.argv[1:]:
        final_text += morse_translator(arg)
        if not arg == sys.argv[-1]:
            final_text += '/ '
except:
    exit("Error")
print(final_text)
    

    
