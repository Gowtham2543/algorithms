# algorithms/bubble_sort/sort.py
from algorithms.bubble_sort.utils import swap

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr
