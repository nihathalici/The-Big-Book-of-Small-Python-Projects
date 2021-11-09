"""Pig Latin, by Al Sweigart al@inventwithpython.com
Translates English messages into Igpay Atinlay.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, word"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def main():
    print('''Igpay Atinlay (Pig Latin)
By Al Sweigart al@inventwithpython.com

Enter your message:''')
    pigLatin = englishToPigLatin(input('> '))

    # Join all the words back together into a single string:
    print(pigLatin)

    try:
        pyperclip.copy(pigLatin)
        print('(Copied pig latin to clipboard.)')
    except NameError:
        pass  # Do nothing if pyperclip wasn't installed.

def englishToPigLatin(message):
    pigLatin = ''  # A string of the pig latin translation.
    for word in message.split():
        # Separate the non-letters at the start of this word:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue

         

if __name__ == '__main__':
    main()
