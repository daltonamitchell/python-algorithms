"""
Write a function, `nearest_larger(arr, i)` which takes an array and an
index.  The function should return another index, `j`: this should
satisfy:

(a) `arr[i] < arr[j]`, AND
(b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j2]`.

In case of ties (see example below), choose the earliest (left-most)
of the two indices. If no number in `arr` is larger than `arr[i]`,
return `nil`.
"""

# pylint: disable=wildcard-import, unused-wildcard-import, undefined-variable
from expects import *

from lib.nearest_larger import nearest_larger

with description('nearest_larger'):
    with it('handles a simple case to the right'):
        expect(nearest_larger([2, 3, 4, 8], 2)).to(equal(3))

    with it('handles a simple case to the left'):
        expect(nearest_larger([2, 8, 4, 3], 2)).to(equal(1))

    with it('treats any two larger numbers like a tie'):
        expect(nearest_larger([2, 6, 4, 8], 2)).to(equal(1))

    with it('should choose the left case in a tie'):
        expect(nearest_larger([2, 6, 4, 6], 2)).to(equal(1))

    with it('finds an answer with a distance greater than 1 to the left'):
        expect(nearest_larger([8, 2, 4, 3], 2)).to(equal(0))

    with it('finds an answer with a distance greater than 1 to the right'):
        expect(nearest_larger([2, 4, 3, 8], 1)).to(equal(3))

    with it('should return None if no larger number is found'):
        expect(nearest_larger([2, 6, 4, 8], 3)).to(equal(None))

    with it('should return the nearer of 2 greater numbers'):
        expect(nearest_larger([2, 6, 9, 4, 8], 3)).to(equal(2))
