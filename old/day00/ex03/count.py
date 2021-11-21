#! /usr/bin/python3

import sys

def text_analyzer(str=""):
    "This function counts the number of uppter characters, lower characters,\
    punctuation and spaces in a given text"
    up = 0
    low = 0
    sp = 0
    marks = 0

    if len(str) == 0:
        str = input("Please, introduce a text to analyze: ")

    for c in str:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isspace():
            sp += 1
        elif not c.isnumeric():
            marks += 1

    print("The text contains", len(str), "characters:\n")
    print("- ", up, "upper letters\n")
    print("- ", low, "lower letters\n")
    print("- ", marks, "punctuation marks\n")
    print("- ", sp, "spaces\n")
    return

