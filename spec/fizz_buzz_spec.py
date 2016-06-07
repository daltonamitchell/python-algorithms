"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For multiples of both three and five print "FizzBuzz".

Your method should optionally take `start` and `end` parameters which add the
following functionality:

start: outputs items from `start` to 100
stop: outputs items from 0 to `end`
start, stop: output items from `start` to `end` inclusive

Of course with no parameters, just output 1 to 100
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.fizz_buzz import fizz_buzz

with description('fizz_buzz'):
    # with _it('returns an array'):
    #   expect(fizz_buzz).to be_a(Array)

    with context('when no parameters are given'):
        with it('outputs 100 items'):
            expect(len(fizz_buzz())).to(equal(100))

        with it('outputs "Fizz" as the third item'):
            EXPECTED = 'Fizz'
            ACTUAL = fizz_buzz()
            expect(ACTUAL[2]).to(equal(EXPECTED))

        with it('outputs "Buzz" as the 5th item'):
            EXPECTED = 'Buzz'
            ACTUAL = fizz_buzz()
            expect(ACTUAL[4]).to(equal(EXPECTED))

        with it('outputs "FizzBuzz" as the 15th item'):
            EXPECTED = 'FizzBuzz'
            ACTUAL = fizz_buzz()
            expect(ACTUAL[14]).to(equal(EXPECTED))

        with it('outputs "Fizz" for every third item'):
            FB = fizz_buzz()
            THIRDS = [FB[i] for i in range(len(FB)) if ((i + 1) % 15 != 0) and ((i + 1) % 3 == 0)]
            ACTUAL = all([(item == 'Fizz') for item in THIRDS])
            expect(ACTUAL).to(equal(True))

        with it('outputs "Buzz" for every fifth item'):
            FB = fizz_buzz()
            FIFTHS = [FB[i] for i in range(len(FB)) if ((i + 1) % 15 != 0) and ((i + 1) % 5 == 0)]
            ACTUAL = all([(item == 'Buzz') for item in FIFTHS])
            expect(ACTUAL).to(equal(True))

        with it('outputs "FizzBuzz" for every fifteenth item'):
            FB = fizz_buzz()
            FIFTEENTHS = [FB[i] for i in range(len(FB)) if (i + 1) % 15 == 0]
            ACTUAL = all([(item == 'FizzBuzz') for item in FIFTEENTHS])
            expect(ACTUAL).to(equal(True))

    with context('when the :start parameter is given'):
        with it('returns 50 items when starting from 51'):
            ACTUAL = fizz_buzz(start=51)
            expect(len(ACTUAL)).to(equal(50))

        with it('returns the last 10 items'):
            # pylint: disable=redefined-variable-type
            EXPECTED = [91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
            ACTUAL = fizz_buzz(start=91)
            expect(EXPECTED).to(equal(ACTUAL))

        with it('can count before 1'):
            ACTUAL = fizz_buzz(start=-5)
            EXPECTED = ['Buzz', -4, 'Fizz', -2, -1]
            expect(len(ACTUAL)).to(equal(106))
            expect(ACTUAL[0:5]).to(equal(EXPECTED))

    with context('when the :stop parameter is given'):
        with it('can only count to 10'):
            ACTUAL = fizz_buzz(end=10)
            expect(len(ACTUAL)).to(equal(10))

        with it('can count past 100'):
            EXPECTED = [101, 'Fizz', 103, 104, 'FizzBuzz']
            ACTUAL = fizz_buzz(end=105)
            expect(len(ACTUAL)).to(equal(105))
            expect(ACTUAL[100:106]).to(equal(EXPECTED))

    with context('when both :start and :stop are given'):
        with it('can still count from 1 to 100'):
            EXPECTED = fizz_buzz()
            ACTUAL = fizz_buzz(start=1, end=100)
            expect(ACTUAL).to(equal(EXPECTED))

        with it('can return only one item'):
            EXPECTED = ['FizzBuzz']
            ACTUAL = fizz_buzz(start=15, end=15)
            expect(ACTUAL).to(equal(EXPECTED))

        with it('correctly returns a range'):
            EXPECTED = ['Buzz', 'Fizz', 37, 38, 'Fizz',
                        'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz']
            ACTUAL = fizz_buzz(start=35, end=45)
            expect(ACTUAL).to(equal(EXPECTED))

        with it('can return a range outside than the default'):
            ACTUAL = fizz_buzz(start=-5, end=105)
            expect(len(ACTUAL)).to(equal(111))
