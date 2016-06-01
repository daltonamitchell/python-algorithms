"""
Write a method that takes in an integer `offset` and a string.
Produce a new string, where each letter is shifted by `offset`. You
may assume that the string contains only lowercase letters and spaces.

When shifting "z" by three letters, wrap around to the front of the
alphabet to produce the letter "c".

You'll want to use String's `ord` method and Integer's `chr` method.
`ord` converts a letter to an ASCII number code. `chr` converts an
ASCII number code to a letter.

You may look at the ASCII printable characters chart:

    http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters

Notice that the letter 'a' has code 97, 'b' has code 98, etc., up to
'z' having code 122.
"""

def caesar_cipher(offset, str):
    chars = [ord(letter) for letter in str]
    return ''.join(encode(char, offset) for char in chars)

def encode(char, offset):
    if char < 97 or char > 122:
        return chr(char)

    char += offset

    if char > 122: char -= 26

    return chr(char)
