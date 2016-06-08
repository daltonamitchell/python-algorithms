"""
Write a method that takes in a string of lowercase letters (no
uppercase letters, no repeats). Consider the *substrings* of the
string: consecutive sequences of letters contained inside the string.
Find the longest such string of letters that is a palindrome.

Note that the entire string may itself be a palindrome.
"""

def is_palindrome(string):
    """Returns whether a given string is a palindrome"""
    return string[::-1] == string


def longest_palindrome(string):
    """Finds the longest substring in a given string that is a palindrome

    Example:

        'abceyefooracecar123' returns 'racecar'
    """
    if is_palindrome(string):
        return string

    max_len = len(string) - 1

    while max_len > 0:
        i = 0
        while (i + max_len) <= len(string):
            sub = string[i:(i + max_len)]
            if is_palindrome(sub):
                return sub
            i += 1
        max_len -= 1
