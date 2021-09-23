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
    pass

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
    
