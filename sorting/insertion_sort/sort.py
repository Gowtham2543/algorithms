# algorithms/insertion_sort/sort.py
from algorithms.insertion_sort.utils import shift_right

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        shift_right(arr, j + 1, i)
        arr[j + 1] = key
    return arr
