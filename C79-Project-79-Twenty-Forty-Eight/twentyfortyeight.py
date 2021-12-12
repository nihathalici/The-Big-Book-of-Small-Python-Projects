"""Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com
A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.
More info at https://en.wikipedia.org/wiki/2048_(video_game)
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, puzzle"""

import random, sys

# Set up the constants:
BLANK = ''  # A value that represents a blank space on the board.

def main():
    print('''Twenty Forty-Eight, by Al Sweigart al@inventwithpython.com

Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up the tiles before then.''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()

    while True:  # Main game loop.
        drawBoard(gameBoard)
        print('Score:', getScore(gameBoard))
        playerMove = askForPlayerMove()
        gameBoard = makeMove(gameBoard, playerMove)
        addTwoToBoard(gameBoard)

        if isFull(gameBoard):
            drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()

def getNewBoard():
    """Returns a new data structure that represents a board.

    It's a dictionary with keys of (x, y) tuples and values of the tile
    at that space. The tile is either a power-of-two integer or BLANK.
    The coordinates are laid out as:
       X0 1 2 3
      Y+-+-+-+-+
      0| | | | |
       +-+-+-+-+
      1| | | | |
       +-+-+-+-+
      2| | | | |
       +-+-+-+-+
      3| | | | |
       +-+-+-+-+"""
    newBoard = {}  # Contains the board data structure to be returned.
    # Loop over every possible space and set all the tiles to blank:
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    # Pick two random spaces for the two starting 2's:
    startingTwosPlaced = 0  # The number of starting spaces picked.
    while startingTwosPlaced < 2:   # Repeat for duplicate spaces.
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        # Make sure the randomly selected space isn't already taken:
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced = startingTwosPlaced + 1

    return newBoard

def drawBoard(board):
    pass

def getScore(board):
    pass

def combineTilesInColumn(column):
    pass

def makeMove(board, move):
    pass

def askForPlayerMove():
    pass

def addTwoToBoard(board):
    pass

def isFull(board):
    pass

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
