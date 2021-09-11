"""Fish Tank, by Al Sweigart al@inventwithpython.com
A peaceful animation of a fish tank. Press Ctrl-C to stop.
Similar to ASCIIQuarium or @EmojiAquarium, but mine is based on an
older ASCII fish tank program for DOS.
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, artistic, bext"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants;
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4

# NOTE: Every string in a fish dictionary should be the same length.
FISH_TYPES = [
    {'right': ['><>'],          'left': ['<><']},
    {'right': ['>||>'],         'left': ['<||<']},
    {'right': ['>))>'],         'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'],        'left': ['<==-<']},
    {'right': [r'>\\>'],        'left': ['<//<']},
    {'right': ['><)))*>'],      'left': ['<*(((><']},
    {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
    {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
    {'right': ['><XXX*>'],      'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>',
               '-._.-._^=>', '._.-._.^=>'],
     'left':  ['<=^-._.-._', '<=^.-._.-.',
               '<=^_.-._.-', '<=^._.-._.']},
    ]

LONGEST_FISH_LENGTH = 10  # Longest single string in FISH_TYPES.

# The x and y positions where a fish runs into the edge of the screen:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # NOTE: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Run the simulation:
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1


def getRandomColor():
    """Return a string of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))

def generateFish():
    """Return a dictionary that represents a fish."""
    fishType = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])
    if colorPattern == 'random':  # All parts are randomly colored.
        colors = []
        for i in range(fishLength):
            colors.append(getRandomColor())
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [getRandomColor()] * fishLength  # All the same color.
    if colorPattern == 'head-tail':  # Head/tail different from body.
        headTailColor = getRandomColor()
        colors[0] = headTailColor  # Set head color.
        colors[-1] = headTailColor  # Set tail color.

    # Set up the rest of fish data structure:
    fish = {'right':               fishType['right'],
            'left':                fishType['left'],
            'colors'               colors,
            'hSpeed':              random.randint(1, 6),
            'vSpeed':              random.randint(5, 15),
            'timeToHDirChange':    random.randint(10, 60),
            'timeToVDirChange':    random.randint(2, 20),
            'goingRight':          random.choice([True, False]),
            'goingDown':           random.choice([True, False])}

    # 'x' is always the leftmost side of the fish body:
    fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish['y'] = random.randint(0, HEIGHT - 2)
    return fish


def simulateAquarium():
    pass

def drawAquarium():
    pass

def clearAquarium():
    pass

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()   # When Ctrl-C is pressed, end the program.
