"""Sudoku Puzzle, by Al Sweigart al@inventwithpython.com
The classic 9x9 number placement puzzle.
More info at https://en.wikipedia.org/wiki/Sudoku
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, object-oriented, puzzle"""

import copy, random, sys

# This game requires a sudokupuzzle.txt file that contains the puzzles.
# Download it from https://inventwithpython.com/sudokupuzzles.txt
# Here's a sample of the content in this file:
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# 2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3
# ......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34.59...5.7......
# .3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.

# Set up the constants:
EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        # originalSetup is a string of 81 characters for the puzzle
        # setup, with numbers and periods (for the blank spaces).
        # See https://inventwithpython.com/sudokupuzzles.txt
        self.originalSetup = originalSetup

        # The state of the sudoku grid is represented by a dictionary
        # with (x, y) keys and values of the number (as a string) at
        # that space.
        self.grid = {}
        self.resetGrid()  # Set the grid state to its original setup.
        self.moves = []  # Tracks each move for the undo feature.


    def resetGrid():
        """Reset the state of the grid, tracked by self.grid, to the
        state in self.originalSetup."""
        for x in range(1, GRID_LENGTH + 1):
            for y in range(1, GRID_LENGTH + 1):
                self.grid[(x, y)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        i = 0  # i goes from 0 to 80
        y = 0  # y goes from 0 to 8
        while i < FULL_GRID_SIZE:
            for x in range(GRID_LENGTH):
                self.grid[(x, y)] = self.originalSetup[i]
                i += 1
            y += 1



    def makeMove(self, column, row, number):
        """Place the number at the column (a letter from A to I) and row
        (an integer from 1 to 9) on the grid."""
        x = 'ABCDEFGHI'.find(column)  # Convert this to an integer.
        y = int(row) - 1

        # Check if the move is being made on a "given" number:
        if self.originalSetup[y * GRID_LENGTH + x] != EMPTY_SPACE:
            return False

        self.grid[(x, y)] = number  # Place this number on the grid.

        # We need to store a separate copy of the dictionary object:
        self.moves.append(copy.copy(self.grid))
        return True

    def undo(self):
        """Set the current grid state to the previous state in the
        self.moves list."""
        if self.moves == []:
            return  # No states in self.moves, so do nothing.

        self.moves.pop()  # Remove the current state.

        if self.moves == []:
            self.resetGrid()
        else:
            # set the grid to the last move.
            self.grid = copy.copy(self.moves[-1])

    def display():
        """Display the current state of the grid on the screen."""
        print('   A B C   D E F   G H I')  # Display column labels.
        for y in range(GRID_LENGTH):
            for x in range(GRID_LENGTH):
                if x == 0:
                    # Display row label:
                    print(str(y + 1) + '  ', end='')

                print(self.grid[(x, y)] + '  ', end='')
                if x == 2 or x == 5:
                    # Display a vertical line:
                    print('| ', end='')
            print()  # Print a newline.
            if y == 2 or y == 5:
                # Display a horizontal line:
                print('   ------+-------+------')

    def _isCompleteSetOfNumbers(self, numbers):
        """Return True if numbers contains the digits 1 through 9."""
        return sorted(numbers) == list('123456789')


    def isSolved(self):
        """Returns True if the current grid is in a solved state."""
        # Check each row:
        for row in range(GRID_LENGTH):
            rowNumbers = []
            for x in range(GRID_LENGTH):
                number = self.grid[(x, row)]
                rowNumbers.append(number)
            if not self._isCompleteSetOfNumbers(rowNumbers):
                return False

        # Check each column:
        for column in range(GRID_LENGTH):
            columnNumbers = []
            for y in range(GRID_LENGTH):
                number = self.grid[(column, y)]
                columnNumbers.append(number)
            if not self._isCompleteSetOfNumbers(columnNumbers):
                return False

        # Check each box:
        for boxx in (0, 3, 6):
            for boxy in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        number = self.grid[(boxx + x, boxy + y)]
                        boxNumbers.append(number)
                if not self._isCompleteSetOfNumbers(boxNumbers):
                    return False

        return True

        
