# algorithms/merge_sort/sort.py
from algorithms.sorting.merge_sort.util import merge

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        merge(arr, L, R)
    return arr
