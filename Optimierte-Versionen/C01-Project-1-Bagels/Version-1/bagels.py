"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""")

    while True:
        secretNum = getSecretNum()
        print(f'I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        for numGuesses in range(1, MAX_GUESSES + 1):
            guess = getValidGuess(numGuesses)
            clues = getClues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break
        else:
            print(f'You ran out of guesses.\nThe answer was {secretNum}.')

        if not input('Do you want to play again? (yes or no): ').lower().startswith('y'):
            break
    
    print('Thanks for playing!')

def getValidGuess(guessNumber):
    """Gets a valid guess from the player."""
    while True:
        guess = input(f'Guess #{guessNumber}: ')
        if len(guess) == NUM_DIGITS and guess.isdecimal():
            return guess
        print(f'Please enter a {NUM_DIGITS}-digit number.')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    return ''.join(random.sample('0123456789', NUM_DIGITS))

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues."""
    if guess == secretNum:
        return 'You got it!'

    clues = []
    secret_set = set(secretNum)
    
    for g_digit, s_digit in zip(guess, secretNum):
        if g_digit == s_digit:
            clues.append('Fermi')
        elif g_digit in secret_set:
            clues.append('Pico')
    
    if not clues:
        return 'Bagels'
    
    clues.sort()
    return ' '.join(clues)

if __name__ == '__main__':
    main()
