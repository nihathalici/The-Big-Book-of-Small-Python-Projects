"""Hourglass, by Al Sweigart al@inventwithpython.com
An animation of an hourglass with falling sand. Press Ctrl-C to stop.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, bext, simulation"""

import random, sys, time

# chq bext module
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.2
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0  # The index of X values in an (x, y) tuple is 0.
Y = 1  # The index of Y values in an (x, y) tuple is 1.
SAND = chr(9617)
WALL = chr(9608)

# Set up the walls of the hourglass:
HOURGLASS = set()  # Has (x, y) tuples for where hourglass walls are.
for i in range(18, 37):
    HOURGLASS.add((i, 1))  # Add walls for the top cap of the hourglass.
    HOURGLASS.add((i, 23))  # Add walls for the bottom cap.

for i in range(1, 5):
    HOURGLASS.add((18, i))  # Add walls for the top left straight wall.
    HOURGLASS.add((36, i))  # Add walls for the top right straight wall.
    HOURGLASS.add((18, i + 19))  # Add walls for the bottom left.
    HOURGLASS.add((36, i + 19))  # Add walls for the bottom right.

for i in range(8):
    HOURGLASS.add((19 + i, 5 + i))  # Add the top left slanted wall.
    HOURGLASS.add((35 - i, 5 + i))  # Add the top right slanted wall.
    HOURGLASS.add((25 - i, 13 + i))  # Add the bottom left slanted wall.
    HOURGLASS.add((29 + i, 13 + i))  # Add the bottom right slanted wall.

# Set up the initial sand at the top of the hourglass:
INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))

        
def main():
    pass

def runHourglassSimulation():
    pass
