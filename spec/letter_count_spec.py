"""
Write a function, `letter_count(str)` that takes a string and
returns a hash mapping each letter to its frequency. Do not include
spaces.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.letter_count import *

with description('letter_count'):
    with it('handles a simple case'):
        EXPECTED = {'c': 1, 'a': 1, 't': 1}
        expect(letter_count('cat')).to(equal(EXPECTED))

    with it('handles multiples of the same letter'):
        EXPECTED = {'m': 1, 'o': 2, 'n': 1}
        expect(letter_count('moon')).to(equal(EXPECTED))

    with it('handles a multi-word case'):
        EXPECTED = {
            'c': 1,
            'a': 2,
            't': 1,
            's': 1,
            'r': 1,
            'e': 1,
            'f': 1,
            'u': 1,
            'n': 1
        }
        expect(letter_count('cats are fun')).to(equal(EXPECTED))
