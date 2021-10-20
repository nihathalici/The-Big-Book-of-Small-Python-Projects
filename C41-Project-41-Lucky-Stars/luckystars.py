"""Lucky Stars, by Al Sweigart al@inventwithpython.com
A "press your luck" game where you roll dice to gather as many stars
as possible. You can roll as many times as you want, but if you roll
hree skulls you lose all your stars.

Inspired by the Zombie Dice game from Steve Jackson Games.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, multiplayer"""

import random

 Set up the constants:
 GOLD = 'GOLD'
 SILVER = 'SILVER'
 BRONZE = 'BRONZE'

 STAR_FACE = ["+-----------+",
              "|     .     |",
              "|    ,O,    |",
              "| 'ooOOOoo' |",
              "|   `OOO`   |",
              "|   O' 'O   |",
              "+-----------+"]
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\  |',
              '|  |() ()|  |',
              '|   \\ ^ /  |',
              '|    VVV    |',
              "+-----------+"]
QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
even.
""")

print('How many players are there?')
while True:  # Loop until the user enters a number.
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        numPlayers = int(response)
        break
    print('Please enter a number larger than 1.')

playerNames = []  # List of strings of player names.
playerScores = {}  # Keys are player names, values are integer scores.
for i in range(numPlayers):
    while True:  # Keep looping until a name is entered.
    print('What is player #' + str(i + 1) + '\'s name?')
    response = input('> ')
    if response != '' and response not in playerNames:
        playerNames.append(response)
        playerScores[response] = 0
        break
    print('Please enter a name.')
print()

turn = 0  # The player at playerNames[0] will go first.
endGameWith = None
while True:  # Main game loop.
    # Display everyone's score:
    print()
    print('SCORES: ', end='')
    for i, name in enumerate(playerNames):
        print(name + ' = ' + str(playerScores[name]), end='')
        if i != len(playerNames) - 1:
            # All but the last player have commas separating their names.
            print(', ', end='')
    print('\n')

    # Start the number of collected stars and skulls at 0.
    stars = 0
    skulls = 0
    # A cup has 6 gold, 4 silver, and 3 bronze dice:
    cup = ([GOLD] * 6) + ([SILVER] = 4) + ([BRONZE] * 3)
    hand = []  # Your hand starts with no dice.
    print('It is ' + playerNames[turn] + '\'s turn.')
    while True:  # Each iteration of this loop is rolling the dice.
      print()
