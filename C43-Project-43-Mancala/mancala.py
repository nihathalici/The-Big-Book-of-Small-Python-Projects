"""Mancala, by Al Sweigart al@inventwithpython.com
The ancient seed-sowing game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, board game, game, two-player"""

import sys

# A tuple of the player's pits:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K'. 'L')

# A dictionary whose keys are pits and values are opposite pit:
OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                   'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D'
                   'K': 'E', 'L': 'F'}

# A dictionary whose keys are pits and values are the next pit in order:
NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

# Every pit label, in counterclockwise order starting with A:
PIT_LABELS = 'ABCDEF1LKJIHG2'

# How many seeds are in each pit at the start of a new game:
STARTING_NUMBER_OF_SEEDS = 4

def main():
        print('''Mancala, by Al Sweigart al@inventwithpython.com

The ancient two-player, seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into your store. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')

    gameBoard = getNewBoard()
    playerTurn = '1'  # Player 1 goes first.

    while True:  # Run a player's turn.
        # "Clear" the screen by printing many newlines, so the old
        # board isn't visible anymore.
        print('\n' * 60)
        # Display board and get the player's move:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(playerTurn, gameBoard)

        # Carry out the player's move:
        playerTurn = makeMove(gameBoard, playerTurn, playerMove)

        # Check if the game ended and a player has won:
        winner = checkForWinner(gameBoard)
        if winner == '1' or winner == '2':
            displayBoard(gameBoard)  # Display the board one last time.
            print('Player ' + winner + ' has won!')
            sys.exit()
        elif winner == 'tie':
            displayBoard(gameBoard)  # Display the board one last time.
            print('There is a tie!')
            sys.exit()

        
def getNewBoard():
    """Return a dictionary representing a Mancala board in the starting
    state: 4 seeds in each pit and 0 in the stores."""

def displayBoard():
    """Displays the game board as ASCII-art based on the board
    dictionary."""

def askForPlayerMove():
    """Asks the player which pit on their side of the board they
    select to sow seeds from. Returns the uppercase letter label of the
    selected pit as a string."""

def makeMove():
    """Modify the board data structure so that the player 1 or 2 in
    turn selected pit as their pit to sow seeds from. Returns either
    '1' or '2' for whose turn it is next."""

def checkForWinner():
    """Looks at board and returns either '1' or '2' if there is a
    winner or 'tie' or 'no winner' if there isn't. The game ends when a
    player's pits are all empty; the other player claims the remaining
    seeds for their store. The winner is whoever has the most seeds."""
