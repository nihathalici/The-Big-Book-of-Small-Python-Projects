"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""

import sys

# (!) Try changing this multiline string to any image you like:
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

def main():
    print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
    print('Enter the message to display with the bitmap.')
    message = input('> ').strip()
    if not message:
        sys.exit()
    
    # Pre-calculate message length and split lines once
    msg_len = len(message)
    lines = bitmap.splitlines()
    
    # Pre-allocate output list for better performance
    output_lines = []
    
    # Process each line
    for line in lines:
        result = []
        # Use list comprehension for faster character processing
        for i, bit in enumerate(line):
            if bit == ' ':
                result.append(' ')
            else:
                result.append(message[i % msg_len])
        output_lines.append(''.join(result))
    
    # Join all lines and print once
    print('\n'.join(output_lines))

if __name__ == '__main__':
    main()
