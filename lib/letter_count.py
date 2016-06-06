"""
Write a function, `letter_count(str)` that takes a string and
returns a hash mapping each letter to its frequency. Do not include
spaces.
"""

from collections import defaultdict

def letter_count(string):
    """Returns a dict with the frequency of each letter in a given string"""
    counts = defaultdict(int) # default new values to 0

    for letter in string.replace(' ', ''):
        counts[letter] += 1

    return counts
