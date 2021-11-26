"""Snail Race, by Al Sweigart al@inventwithpython.com
Fast-paced snail racing action!
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, artistic, beginner, game, multiplayer"""

import random, time, sys

# Set up the constatnts:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

print('''Snail Race, by Al Sweigart al@inventwithpython.com

    @v <-- snail

''')

# Ask how many snails to race:
while True:  # Keep asking until the player enters a number.
    print('How many snails will race? Max:', MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing <= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and', MAX_NUM_SNAILS)
