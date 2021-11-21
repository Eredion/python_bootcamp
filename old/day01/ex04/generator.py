#! /usr/bin/env python3

import random

def generator(text, sep=" ", option=None):
    words = text.split(sep)
    if option == 'ordered':
        words.sort()
    elif option == 'shuffle':
        rnum = []
        words_copy = []
        for i in range(0, len(words)):
            ok = 0
            while ok == 0:
                num = random.randint(0, len(words) - 1)
                if num not in rnum:
                    rnum.append(num)
                    ok = 1
        for i in rnum:
            words_copy.append(words[i])
        words = words_copy            
    elif option == 'unique':
        words_copy = []
        for word in words:
            if word not in words_copy:
                words_copy.append(word)
        words = words_copy
    for word in words:
        yield word


texto = "Vamos a hacer una hacer primera prueba hacer una primera a prueba"
print("UNIQUE")
for word in generator(texto, sep = " ", option='unique'):
    print(word)
print("\nSHUFFLE")
for word in generator(texto, sep = " ", option='shuffle'):
    print(word)
print("\nORDERED")
for word in generator(texto, sep = " ", option='ordered'):
    print(word)
