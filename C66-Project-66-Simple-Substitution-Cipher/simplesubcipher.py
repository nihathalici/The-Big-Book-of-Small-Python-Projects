"""Simple Substitution Cipher, by Al Sweigart al@inventwithpython.com
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
More info at: https://en.wikipedia.org/wiki/Substitution_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, cryptography, math"""

import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
        pass

def checkKey(key):
    pass

def encryptMessage(message, key):
    pass

def decryptMessage(message, key):
    pass

def translateMessage(message, key, mode):
    pass

def generateRandomKey():
    pass

# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
