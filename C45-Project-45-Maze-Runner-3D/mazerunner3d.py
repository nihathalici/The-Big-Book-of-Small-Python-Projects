"""Maze 3D, by Al Sweigart al@inventwithpython.com
Move around a maze and try to escape... in 3D!
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: extra-large, artistic, maze, game"""

import copy, sys, os

# Set up the constants:
WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)  # Character 9617 is '░'
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

def wallStrToWallDict(wallStr):
    """Takes a string representation of a wall drawing (like those in
    ALL_OPEN or CLOSED) and returns a representation in a dictionary
    with (x, y) tuples as keys and single-character strings of the
    character to draw at that x, y location."""
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wallDict[(x, y)] = character
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

# The way we create the strings to display is by converting the pictures
# in these multiline strings to dictionaries using wallStrToWallDict().
# Then we compose the wall for the player's location and direction by
# "pasting" the wall dictionaries in CLOSED on top of the wall dictionary
# in ALL_OPEN.

ALL_OPEN = wallStrToWallDict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())
# The strip() call is used to remove the newline
# at the start of this multiline string.

CLOSED = {}
CLOSED['A'] = wallStrToWallDict(r'''
_____
.....
.....
.....
_____'''.strip())  # Paste to 6, 4.

CLOSED['B'] = wallStrToWallDict(r'''
.\.
..\
...
...
...
../
./.'''.strip())  # Paste to 4, 3.

CLOSED['C'] = wallStrToWallDict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())  # Paste to 3, 1.

CLOSED['D'] = wallStrToWallDict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())  # Paste to 10, 3.

CLOSED['E'] = wallStrToWallDict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())  # Paste to 0, 0.

CLOSED['F'] = wallStrToWallDict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())  # Paste to 12, 0.


def displayWallDict(wallDict):
    """Display a wall dictionary, as returned by wallStrToWallDict(), on
    the screen."""
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            wall = wallDict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print(BLOCK)   # Print block with a newline.
    print(BLOCK * (wallDict['width'] + 2))

def pasteWallDict(srcWallDict, dstWallDict, left, top):
    """Copy the wall representation dictionary in srcWallDict on top of
    the one in dstWallDict, offset to the position given by left, top."""
    dstWallDict = copy.copy(dstWallDict)
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict

def makeWallDict(maze, playerx, playery, playerDirection, exitx, exity):
    """From the player's position and direction in the maze (which has
    an exit at exitx, exity), create the wall representation dictionary
    by pasting wall dictionaries on top of ALL_OPEN, then return it."""

    # The A-F "sections" (which are relative to the player's direction)
    # determine which walls in the maze we check to see if we need to
    # paste them over the wall representation dictionary we're creating.

    if playerDirection == NORTH:
        # Map of the sections, relative  A
        # to the player @:              BCD (Player facing north)
        #                               E@F
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        # Map of the sections, relative  F@E
        # to the player @:               DCB (Player facing south)
        #                                 A
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        # Map of the sections, relative  EB
        # to the player @:               @CA (Player facing east)
        #                                FD
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        # Map of the sections, relative  DF
        # to the player @:               AC@ (Player facing west)
        #                                BE
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerx + xOff, playery + yOff), WALL)
        if (playerx + xOff, playery + yOff) == (exitx, exity):
            section[sec] = EXIT
