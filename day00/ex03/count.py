import sys

def empty_text():
    print("What is the text to analyse?")
    text = sys.stdin.readlines()
    text_analyzer(text)

def text_analyzer(text=None):
    """text_analyzer analyzes the characteres of a given text"""
    if text is None:
        empty_text()
        return
    upp = 0
    low = 0
    sp = 0
    mark = 0
    for i in text:
        if i.isupper() == True:
            upp += 1
        elif i.islower() == True:
            low += 1
        elif i.isspace() == True:
            sp += 1
        elif i.isnumeric() == False:
            mark += 1

    print("The text contains", len(text), "characters:\n")
    print("- ", upp ," upper letters\n")
    print("- ", low ," lower letters\n")
    print("- ", mark ," punctuation marks letters\n")
    print("- ", sp ," spaces letters\n")

