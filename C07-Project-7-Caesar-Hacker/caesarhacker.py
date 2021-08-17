"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com
This program hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.
More info at:
https://en.wikipedia.org/wiki/Caesar_cipher#Breaking_the_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key.
for key in range(len(SYMBOLS)):
    translated = ''

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            # Get the number of the symbol.
            num = SYMBOLS.find(symbol)
            # Decrypt the number.
            num = num - key

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))
