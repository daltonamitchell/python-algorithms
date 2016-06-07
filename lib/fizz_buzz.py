"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For multiples of both three and five print "FizzBuzz".

Your method should optionally take `start` and `end` parameters which add the
following functionality:

start: outputs items from `start` to 100
stop: outputs items from 1 to `end`
start, stop: output items from `start` to `end` inclusive

Of course with no parameters, just output 1 to 100
"""


def fizz_buzz(start=1, end=100):
    """
    Returns a list between start and end (inclusive) with the
    following values:

    'Fizz' for every 3rd item
    'Buzz' for every 5th item
    'FizzBuzz' for every 15th item
    Just the number for everything else
    """
    fizzbuzz = lambda i: 'FizzBuzz' if i % 15 == 0 else None
    fizz = lambda i: 'Fizz' if i % 3 == 0 else None
    buzz = lambda i: 'Buzz' if i % 5 == 0 else None
    position_check = lambda i: fizzbuzz(i) or fizz(i) or buzz(i) or i

    return [position_check(i) for i in range(start, (end + 1))]
