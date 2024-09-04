# algorithms/selection_sort/utils.py
def find_min_index(arr, start):
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
