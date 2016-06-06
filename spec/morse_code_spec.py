"""
Build a function, `morse_encode(str)` that takes in a string (no
numbers or punctuation) and outputs the morse code for it.

See http://en.wikipedia.org/wiki/Morse_code.

Put two spaces between words and one space between letters.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.morse_code import morse_encode

with description('morse_encode'):
    with it('encodes a simple letter'):
        expect(morse_encode('q')).to(equal('--.-'))

    with it('encodes a small word'):
        expect(morse_encode('cat')).to(equal('-.-. .- -'))

    with it('encodes a phrase'):
        expect(morse_encode('cat in hat')).to(equal('-.-. .- -  .. -.  .... .- -'))
