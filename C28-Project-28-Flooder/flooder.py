"""Flooder, by Al Sweigart al@inventwithpython.com
A colorful game where you try to fill the board with a single color. Has
a mode for colorblind players.
Inspired by the "Flood It!" game.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, bext, game"""

import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

# Constants for the different shapes used in colorblind mode:
HEART = chr(9829)  # Character 9829 is '♥'.
DIAMOND = chr(9830)  # Character 9830 is '♦'.
SPADE = chr(9824)  # Character 9824 is '♠'.
CLUB = chr(9827)  # Character 9827 is '♣'.
BALL = chr(9679)  # Character 9679 is '•'.
TRIANGLE = chr(9650)  # Character 9650 is '▲'.

BLOCK = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT = chr(9488)  # Character 9488 is '┐'
UPRIGHT = chr(9492)  # Character 9492 is '└'
UPLEFT = chr(9496)  # Character 9496 is '┘'
# A list of chr() codes is at https://inventwithpython.com/chr

# All the color/shape tiles used on the board:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2: 'blue',
              3: 'yellow', 4: 'cyan', 5: 'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'    

def main():
    pass

def getNewBoard():
    pass

def displayBoard():
    pass

def askForPlayerMove():
    pass

def changeTile():
    pass

def hasWon():
    pass
