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


