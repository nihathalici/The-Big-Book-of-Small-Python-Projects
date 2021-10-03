"""Hungry Robots, by Al Sweigart al@inventwithpython.com
Escape the hungry robots by making them crash into each other.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game"""

import random, sys

# Set up the constants:
WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

WALL = chr(9617)

def main():
    print('''Hungry Robots, by Al Sweigart al@inventwithpython.com

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
'''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # Set up a new game:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True:   # Main game loop.
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0:   # Check if the player has won.
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # Move the player and robots:
        playerPosition = askForPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots:   # Check if the player has lost.
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()

def getNewBoard():
    pass

def getRandomEmptySpace():
    pass

def isEmpty():
    pass

def addRobots():
    pass

def displayBoard():
    pass

def askForPlayerMove():
    pass

def moveRobots():
    pass
