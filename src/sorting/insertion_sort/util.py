# algorithms/insertion_sort/utils.py
def shift_right(arr, start, end):
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]
