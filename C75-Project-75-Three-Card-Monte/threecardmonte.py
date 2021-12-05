"""Three-Card Monte, by Al Sweigart al@inventwithpython.com
Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you
always lose.)
More info at https://en.wikipedia.org/wiki/Three-card_Monte
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, card game, game"""

import random, time

# Set up the constants:
NUM_SWAPS = 16
DELAY     = 0.8

# The card suit characters:
HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

# The indexes of a 3-card list:
LEFT   = 0
MIDDLE = 1
RIGHT  = 2

def displayCards():
    pass

def getRandomCard():
    pass
