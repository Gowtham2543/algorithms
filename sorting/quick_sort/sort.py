# algorithms/quick_sort/sort.py
from algorithms.quick_sort.utils import partition

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = partition(arr, pivot)
    return quick_sort(left) + middle + quick_sort(right)
