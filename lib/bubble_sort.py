"""
Write a function `bubble_sort(arr)` which will sort an array of
integers using the "bubble sort"
methodology. (http://en.wikipedia.org/wiki/Bubble_sort)
"""

def bubble_sort(arr):
    """Sort an array using the bubble_sort method"""
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        i = 1
        while i < len(arr):
            if arr[i-1] > arr[i]:
                is_sorted = False
                arr[i-1], arr[i] = arr[i], arr[i-1]
            i += 1

    return arr
