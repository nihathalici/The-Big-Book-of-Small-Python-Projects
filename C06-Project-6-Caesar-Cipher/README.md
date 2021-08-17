Caesar Cipher
========================================================

The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. 

caesarcipher.py
========================================================

```Python3
"""Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    # pyperclip copies text to the clipboard.
    import pyperclip
except ImportError:
    # If pyperclip is not installed, do nothing. It's no big deal.
    pass

# Every possible symbol that can be encrypted/decrypted:
# (!) You can add numbers and punctuation marks to encrypt those
# symbols as well.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
# Keep asking until the user enters e or d.
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter the key to use:
# Keep asking until the user enters a valid key.
while True:
    maxKey= len(SYMBOLS) - 1
    print('Please enter the key (0 to {})'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) <= len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}'.format(mode))
message = input('> ')

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores the encrypted/decrypted form of the message:
translated = ''

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num = SYMBOLS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        # Handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    # Do nothing if pyperclip wasn't installed.
    pass

```

Sample Output
========================================================

The player’s input is marked in bold.

![Sample output Caesar Cipher](https://github.com/nihathalici/The-Big-Book-of-Small-Python-Projects/blob/main/C06-Project-6-Caesar-Cipher/caesarscipher_sample_output.PNG)
