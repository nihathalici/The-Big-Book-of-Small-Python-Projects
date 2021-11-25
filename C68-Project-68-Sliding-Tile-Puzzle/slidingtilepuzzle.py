"""Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com
Slide the numbered tiles into the correct order.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, puzzle"""

import random, sys

BLANK = '  '


def main():
    print('''Sliding Tile Puzzle, by Al Sweigart al@inventwithpython.com

    Use the WASD keys to move the tiles
    back into their original order:
           1  2  3  4
           5  6  7  8
           9 10 11 12
          13 14 15   ''')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()

def getNewBoard():
    pass

def displayBoard(board):
    pass

def findBlackSpace(board):
    pass

def askForPlayerMove(board):
    pass

def makeMove(board, move):
    pass

def makeRandomMove(board):
    pass

def getNewPuzzle(moves=200):
    pass
    
