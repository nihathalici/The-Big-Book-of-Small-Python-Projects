"""Four in a Row, by Al Sweigart al@inventwithpython.com
A tile-dropping game to get four in a row, similar to Connect Four.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, board game, two-player"""

import sys

# Constants used for displaying the board:
EMPTY_SPACE = '.'  # A period is easier to count than a space.
PLAYER_X = 'X'
PLAYER_O = 'O'

 # Note: Update displayBoard() & COLUMN_LABELS if BOARD_WIDTH is changed.
 BOARD_WIDTH = 7
 BOARD_HEIGHT = 6
 COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
 assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    print("""Four in a Row, by Al Sweigart al@inventwithpython.com

Two players take turns dropping tiles into one of seven columns, trying
to make four in a row horizontally, vertically, or diagonally.
""")
    # Set up a new game:
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    while True:  # Run a player's turn.
        # Display the board and get player's move.
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Check for a win or tie:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # Display the board one last time.
            print('Ther is a tie!')
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X

def getNewBoard():
    """Returns a dictionary that represents a Four in a Row board.
    The keys are (columnIndex, rowIndex) tuples of two integers, and the
    values are one of the 'X', 'O' or '.' (empty space) strings."""
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def displayBoard():
    """Display the board and its tiles on the screen."""

    '''Prepare a list to pass to the format() string method for the
    board template. The list holds all of the board's tiles (and empty
    spaces) going left to right, top to bottom:'''
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # Display the board:
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tileChars))

def askForPlayerMove(playerTile, board):
    """Let a player select a column on the board to drop a tile into.

    Returns a tuple of the (column, row) that the tile falls into."""
    while True:  # Keep asking player until they enter a valid move.
        print('Player {}, enter a column or QUIT:'.format(playerTile))
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if response not in COLUMN_LABELS:
            print('Enter a number from 1 to {}.'.format(BOARD_WIDTH))
            continue  # Ask player again for their move.

        columnIndex = int(response) - 1  # -1 for 0-based the index.

        # If the column is full, ask for a move again:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print('That column is full, select another one.')
            continue  # Ask player again for their move.

        # Starting from the bottom, find the first empty space.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    pass

def isWinner(playerTile, board):
    pass

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
