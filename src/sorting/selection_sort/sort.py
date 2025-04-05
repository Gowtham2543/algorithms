# algorithms/selection_sort/sort.py
from sorting.selection_sort.util import find_min_index, swap

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = find_min_index(arr, i)
        swap(arr, i, min_idx)
    return arr
