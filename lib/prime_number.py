"""
Is Prime

Write a method that takes in an integer (greater than one) and
returns true if it is prime otherwise return false.

nth Prime

Write a method that returns the `n`th prime number. Recall that only
numbers greater than 1 can be prime.
"""

from math import sqrt


def is_prime(num):
    """Determines whether a given number is prime"""
    if num < 2:
        return False
    if num < 4:
        return True

    i = 1
    while i <= sqrt(num):
        i += 1
        if even_above_two(i):
            continue
        if num % i == 0:
            return False

    return True


def nth_prime(num):
    """Finds the nth number in sequence of all prime numbers"""
    i = 1
    checked = 0
    while checked < num:
        i += 1
        if even_above_two(i):
            continue
        if is_prime(i):
            checked += 1

    return i


def even_above_two(num):
    """Determines if numbers above 2 are even"""
    return not bool(num & 1) and num != 2
