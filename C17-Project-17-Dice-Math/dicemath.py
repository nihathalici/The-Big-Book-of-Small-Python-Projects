"""Dice Math, by Al Sweigart al@inventwithpython.com
A flash card addition game where you sum the total on random dice rolls.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, math"""

import random, time

# Set up the constants:
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3   # -3 for room to enter the sum at the bottom.

# The duration is in seconds:
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4  # Points awarded for correct answers.
PENALTY = 1  # (!) Points removed for incorrect answers.

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 =  (['+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'], 4)

D5 =  (['+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'], 5)

D6a =  (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)


ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Al Sweigart al@inventwithpython.com

Add up the sides of all the dice displayed on the screen. You have
{} seconds to answer as many as possible. You get {} points for each
correct answer and lose {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

