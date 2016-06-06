"""
Return the factorial of the provided integer. If the integer is represented
with the letter n, a factorial is the product of all positive integers less
than or equal to n.

Factorials are often represented with the shorthand notation n!

For example: 5! = 1 * 2 * 3 * 4 * 5 = 120
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.factorial import factorial

with description('factorial'):
    with it('returns 1 for 0'):
        expect(factorial(0)).to(equal(1))

    with it('returns the input for 1 or 2'):
        expect(factorial(1)).to(equal(1))
        expect(factorial(2)).to(equal(2))

    with it('returns 24 for 4'):
        expect(factorial(4)).to(equal(24))

    with it('returns 3,628,800 for 10'):
        expect(factorial(10)).to(equal(3628800))

    with it('returns 2,432,902,008,176,640,000 for 20'):
        expect(factorial(20)).to(equal(2432902008176640000))
