Digital Stream
========================================================
This program mimics the “digital stream” visualization from the science fiction movie The Matrix. 

digitalstream.py
========================================================
```Python3
"""Digital Stream, by Al Sweigart al@inventwithpython.com
A screensaver in the style of The Matrix movie's visuals.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, artistic, beginner, scrolling"""

import random, shutil, sys, time

# Set up the constants:
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ['ㅅ', 'ㅕ']

# Density can range from 0.0 to 1.0:
DENSITY = 0.02

# Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]

# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Digital Stream, by Al Sweigart al@inventwithpython.com')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            # Display an empty space or a 1/0 character.
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end = '')
                columns[i] -= 1
            else:
                print(' ', end = '')
        print()  # Print a newline at the end of the row of columns.
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
                          
```

Sample Output
========================================================

![Sample output Digital Clock](https://github.com/nihathalici/The-Big-Book-of-Small-Python-Projects/blob/main/C20-Project-20-Digital-Stream/digitalstream_sample_output.PNG)
