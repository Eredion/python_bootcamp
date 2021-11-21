#!/usr/bin/env python

def text_analyzer(*args):
    """
    This function alnalyze the text given as argument.
    """
    if len(args) == 0:
        print("What is the text to analyze?")
        text = input()
    elif len(args) > 1:
        exit("ERROR")
    else:
        text = args[0]

    sp = pm = uc = lc = 0
    for i in text:
        if i.isspace():
            sp+= 1
        elif i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
        else:
            pm += 1

    print("The text contans {len} characters:".format(len=len(text)))
    print("- ", uc, "upper letters")
    print("- ", lc, "lower letters")
    print("- ", pm, "punctuation marks")
    print("- ", sp, "spaces")

