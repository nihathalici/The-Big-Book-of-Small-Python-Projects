"""Langton's Ant, by Al Sweigart al@inventwithpython.com
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext, simulation"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
HEIGHT -= 1  # Adjustment for the quit message at the bottom.

NUMBER_OF_ANTS = 10
PAUSE_AMOUNT = 0.1

ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

def main():
    pass

def displayBoard(board, ants, changedTiles):
    """Displays the board and ants on the screen. The changedTiles
    argument is a list of (x, y) tuples for tiles on the screen that
    have changed and need to be redrawn."""
    pass
