"""J'ACCUSE!, by Al Sweigart al@inventwithpython.com
A mystery game of intrigue and a missing cat.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, game, humor, puzzle"""

# Play the original Flash game at:
# https://homestarrunner.com/videlectrix/wheresanegg.html
# More info at: http://www.hrwiki.org/wiki/Where's_an_Egg%3F

import time, random, sys

# Set up the constants:
SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT',
'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE',
'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY',
'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

knownSuspectsAndItems = []
# visitedPlaces: Keys=places, values=strings of the suspect & item there.
visitedPlaces = {}
currentLocation = 'TAXI'  # Start the game at taxi.
accusedSuspects = []  # Accused suspects won't offer clues.
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3  # You can accuse up to 3 people.
culprit = random.choice(SUSPECTS)

# Common indexes link these; e.g. SUSPECTS[0] and ITEMS[0] are at PLACES[0].
random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

# Create data structures for clues the truth-tellers give about each
# item and suspect.
# clues: Keys=suspects being asked for a clue, value="clue dictionary".
clues = {}
for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue

    # This "clue dictionary" has keys=items & suspects,
    # value=the clue given.
    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False  # Useful for debugging.
    for item in ITEMS:  # Select clue about each item.
        if random.randint(0, 1) == 0:  # Tells where the item is:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:  # Tells who has the item:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:  # Select clue about each suspect.
        if random.randint(0, 1) == 0:  # Tells where the suspect is:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:  # Tells what item the suspect has:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]
