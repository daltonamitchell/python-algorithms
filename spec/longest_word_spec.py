"""
Write a method that takes in a string. Return the longest word in
the string.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.longest_word import longest_word

with description('longest_word'):
    with it('handles a simple string'):
        expect(longest_word('short longest')).to(equal('longest'))

    with it('handles only one word'):
        expect(longest_word('one')).to(equal('one'))

    with it('handles many words'):
        expect(longest_word('is the loneliest number')).to(equal('loneliest'))

    with it('handles punctuation'):
        expect(longest_word('Hi there, how are you?')).to(equal('there'))

    with it('returns the first longest if more than one'):
        expect(longest_word('Four score and seven years ago...')).to(equal('score'))
