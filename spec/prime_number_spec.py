"""
Is Prime

Write a method that takes in an integer (greater than one) and
returns true if it is prime otherwise return false.

nth Prime

Write a method that returns the `n`th prime number. Recall that only
numbers greater than 1 can be prime.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.prime_number import is_prime, nth_prime


with description('is_prime'):
    with it('returns false for 1'):
        expect(is_prime(1)).to(be_false)

    with it('returns true for 2 or 3'):
        expect(is_prime(2)).to(be_true)
        expect(is_prime(3)).to(be_true)

    with it('handles_other_examples'):
        expect(is_prime(4)).to(be_false)
        expect(is_prime(9)).to(be_false)
        expect(is_prime(17)).to(be_true)
        expect(is_prime(100)).to(be_false)


with description('nth_prime'):
    with it('finds the 1st prime number'):
        expect(nth_prime(1)).to(equal(2))

    with it('finds the 2nd prime number'):
        expect(nth_prime(2)).to(equal(3))

    with it('finds prime numbers 3 thru 5'):
        expect(nth_prime(3)).to(equal(5))
        expect(nth_prime(4)).to(equal(7))
        expect(nth_prime(5)).to(equal(11))
