#! /usr/bin/python3

import sys
import random

n = random.randint(1, 99)
attemps = 0
print ('This is an interactive guessing game!')
print ('You have to enter a number between 1 and 99 to find out the secre number.')
print('Type \'exit\' to end the game.\nGood luck!')

while True:
    print("What's your guess between 1 and 99?")
    guess = input()
    attemps += 1
    ex = 0
    try:
        guess = int(guess)
        if guess > n:
            print('Too high!')
        elif guess < n:
            print('Too low!')
        elif guess == n:
            if n == 42:
                print('The answer to the ultimate question of life, the universe\
                      and everything is 42.')
            if attemps == 1:
                print('Congratulations! You got it on your first try!')
            else:
                print("Congratulations, you've got it!\nYou won in "+ str(attemps) + " attempts!")
            ex = 1
    except:
        if guess == 'exit':
            ex = 1
        else:
            print('That\'s not a number.')
    if ex == 1:
        exit('Goodbye!')
    

