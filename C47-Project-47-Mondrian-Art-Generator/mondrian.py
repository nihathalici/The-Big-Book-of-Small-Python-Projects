"""Mondrian Art Generator, by Al Sweigart al@inventwithpython.com
Randomly generates art in the style of Piet Mondrian.
More info at: https://en.wikipedia.org/wiki/Piet_Mondrian
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, bext"""

import sys, random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:

# Setup the screen:
