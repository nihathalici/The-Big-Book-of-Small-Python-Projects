"""Three-Card Monte, by Al Sweigart al@inventwithpython.com
Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you
always lose.)
More info at https://en.wikipedia.org/wiki/Three-card_Monte
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, card game, game"""

import random, time

# Set up the constants:
NUM_SWAPS = 16
DELAY     = 0.8

# The card suit characters:
HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

# The indexes of a 3-card list:
LEFT   = 0
MIDDLE = 1
RIGHT  = 2

def displayCards(cards):
    """Display the cards in "cards", which is a list of (rank, suit)
    tuples."""
    rows = ['', '', '', '', '']  # Stores the text to display.

    for i, card in enumerate(cards):
        rank, suit = card  # The card is a tuple data structure.
        rows[0] += ' ___  '  # Print the top line of the card.
        rows[1] += |{} | '.format(rank.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for i in range(5):
        print(rows[i])

def getRandomCard():
    """Returns a random card that is NOT the Queen of Hearts."""
    while True:   # Make cards until you get a non-Queen of hearts.
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

        # Return the card as long as it's not the Queen of Hearts:
        if rank != 'Q' and suit != HEARTS:
            return (rank, suit)

print('Three-Card Monte, by Al Sweigart al@inventwithpython.com')
print()
print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
print('the cards move.')
print()
