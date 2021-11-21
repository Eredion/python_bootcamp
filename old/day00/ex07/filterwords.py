#! /usr/bin/python3

import sys
import string

def filter_words(str, n):
    for i in string.punctuation :
        str.replace(i, ' ')
    words = str.split(" ")
    filtered = []
    for word in words:
        if len(word) >= n:
            filtered.append(word)
    print(filtered)

if __name__ == '__main__':
    try:
        filter_words(str(sys.argv[1]), int(sys.argv[2]))
    except:
        exit("Error")
    exit()

