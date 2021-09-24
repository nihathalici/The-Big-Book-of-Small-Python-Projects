"""Hacking Minigame, by Al Sweigart al@inventwithpython.com
The hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, artistic, game, puzzle"""

import random, sys

# Set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()

def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # The computer memory" is just cosmetic, but it looks cool:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Start at 4 tries remaining, going down:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S   G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))



def getWords():
    pass

def getOneWordExcept():
    pass

def numMatchingLetters():
    pass

def getComputerMemoryString():
    pass

def askForPlayerGuess():
    pass

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt():
        sys.exit()  # When Ctrl-C is pressed, end the program.
