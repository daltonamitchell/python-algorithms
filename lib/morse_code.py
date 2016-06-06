"""
Build a function, `morse_encode(str)` that takes in a string (no
numbers or punctuation) and outputs the morse code for it.

See http://en.wikipedia.org/wiki/Morse_code.

Put two spaces between words and one space between letters.
"""

MORSE_CODE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

def morse_encode(string):
    """Converts a string to morse code"""
    words = [morse_encode_word(word) for word in string.split(' ')]
    return '  '.join(words)


def morse_encode_word(word):
    """Converts a single word to morse code"""
    letters = [MORSE_CODE[letter] for letter in word]
    return ' '.join(letters)
