"""
Write a method that takes in a string. Return the longest word in
the string.
"""

from re import sub as replace

def longest_word(string):
    """Finds the longest word in a given string"""
    if len(string) == 1:
        return string

    # split string and remove any non-alphanum chars
    words = [replace(r'[\W+]', '', word) for word in string.split(' ')]

    if len(words) == 1:
        return string

    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
