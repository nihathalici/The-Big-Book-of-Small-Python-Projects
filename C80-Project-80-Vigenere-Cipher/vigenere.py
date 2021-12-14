"""Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Vigenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.
More info at: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, cryptography, math"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print('''Vigenère Cipher, by Al Sweigart al@inventwithpython.com
The Viegenère cipher is a polyalphabetic substitution cipher that was
powerful enough to remain unbroken for centuries.''')

    # Let the user specify if they are encrypting or decrypting:
    while True:  # Keep asking until the user enters e or d.
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    # Let the user specify the key to use:
    while True:  # Keep asking until the user enters a valid key.
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        response = input('> ').upper()
        if response.isalpha():
            myKey = response
            break

    # Let the user specify the message to encrypt/decrypt:
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('> ')

    # Perform the encryption/decryption:
    if myMode == 'encrypt':
        translated = encryptMessage(myMessage, myKey)
    elif myMode == 'decrypt':
        translated = decryptMessage(myMessage, myKey)

    print('%sed message:' % (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied to clipboard.' % (myMode))
    except:
        pass  # Do nothing if pyperclip wasn't installed. 



def encryptMessage(message, key):
    pass

def decryptMessage(message, key):
    pass

def translateMessage(message, key, mode):
    pass


# If this program was run (instead of imported), run the program:
if __name__ == '__main__':
    main()
