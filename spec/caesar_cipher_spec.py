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

from expects import *

from lib.caesar_cipher import caesar_cipher

with description('caesar_cipher'):
    with it('converts a single letter'):
        expect(caesar_cipher(2, 'a')).to(equal('c'))

    with it('converts a simple string'):
        expect(caesar_cipher(3, 'abc')).to(equal('def'))

    with it('converts a complex string'):
        original = 'the quick brown fox jumps over the lazy dog'
        expected = 'ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl'
        expect(caesar_cipher(5, original)).to(equal(expected))
