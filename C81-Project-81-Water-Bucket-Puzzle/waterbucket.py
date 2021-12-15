"""Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com
A water pouring puzzle.
More info: https://en.wikipedia.org/wiki/Water_pouring_puzzle
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, game, math, puzzle"""

import sys


print('Water Bucket Puzzle, by Al Sweigart al@inventwithpython.com')

GOAL = 4  # The exact amount of water to have in a bucket to win.
steps = 0  # Keep track of how many steps the player made to solve this.

# The amount of water in each bucket:
waterInBucket = {'8': 0, '5': 0, '3': 0}

while True:  # Main game loop.
    # Display the current state of the buckets:
    print()
    print('Try to get ' + str(GOAL) + 'L of water into one of these')
    print('buckets:')

    waterDisplay = []  # Contains strings for water or empty space.

    # Get the strings for the 8L bucket:
    for i in range(1, 9):
        if waterInBucket['8'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Get the strings for the 5L bucket:
    for i in range(1, 6):
        if waterInBucket['5'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Get the strings for the 3L bucket:
    for i in range(1, 4):
        if waterInBucket['3'] < i:
            waterDisplay.append('      ')  # Add empty space.
        else:
            waterDisplay.append('WWWWWW')  # Add water.

    # Display the buckets with the amount of water in each one:
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterDisplay))

    # Check if any of the buckets has the goal amount of water:
    for waterAmount in waterInBucket.values():
        if waterAmount == GOAL:
            print('Good job! You solved it in', steps, 'steps!')
            sys.exit()

    # Let the player select an action to do with a bucket:
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    
