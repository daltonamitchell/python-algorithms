"""
Write a function, `nearest_larger(arr, i)` which takes an array and an
index.  The function should return another index, `j`: this should
satisfy:

(a) `arr[i] < arr[j]`, AND
(b) there is no `j2` closer to `i` than `j` where `arr[i] < arr[j2]`.

In case of ties (see example below), choose the earliest (left-most)
of the two indices. If no number in `arr` is larger than `arr[i]`,
return `None`.
"""


def nearest_larger(arr, i):
    """Finds the nearest item in `arr` which is larger than arr[i]"""
    distance = 1

    while True:
        left = i - distance
        right = i + distance

        if (left < 0) and (right >= len(arr)):
            return None
        if (left >= 0) and (arr[left] > arr[i]):
            return left
        if (right < len(arr)) and (arr[right] > arr[i]):
            return right

        distance += 1

    return None
