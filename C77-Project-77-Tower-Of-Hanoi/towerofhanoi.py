"""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com
A stack-moving puzzle game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, game, puzzle"""

import copy
import sys

TOTAL_DISKS = 5  # More disks means a more difficult puzzle.

# Start with all disks on tower A:
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))

def main():
    print("""The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""
    )

    # Set up the towers. The end of the list is the top of the tower.
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:  # Run a single turn.
        # Display the towers and disks:
        displayTowers(towers)

        # Ask the user for a move:
        fromTower, toTower = askForPlayerMove(towers)

        # Move the top disk from fromTower to toTower:
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Check if the user has solved the puzzle:
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers  # Display the towers one last time.
            print('You have solved the puzzle! Well done!')
            sys.exit()

def askForPlayerMove(towers):
    pass

def displayTowers(towers):
    pass

def displayDisk(width):
    pass

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
