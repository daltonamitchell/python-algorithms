"""
Write a function `bubble_sort(arr)` which will sort an array of
integers using the "bubble sort"
methodology. (http://en.wikipedia.org/wiki/Bubble_sort)
"""

from expects import *

from lib.bubble_sort import *

with description('bubble_sort'):
    with it('works with an empty array'):
        expect(bubble_sort([])).to(equal([]))

    with it('works with an array of 1 item'):
        expect(bubble_sort([1])).to(equal([1]))

    with it('sorts a small array of numbers'):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        expect(bubble_sort(arr)).to(equal(expected))

    with it('sorts a larger array'):
        arr = [9, 10, 3, 1, 4, 17, 23, 12, 25, 6]
        expected = [1, 3, 4, 6, 9, 10, 12, 17, 23, 25]
        expect(bubble_sort(arr)).to(equal(expected))
