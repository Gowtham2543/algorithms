# algorithms/selection_sort/tests/util.py
from sorting.selection_sort.util import find_min_index, swap

def test_find_min_index():
    arr = [64, 25, 12, 22, 11, 90]
    assert find_min_index(arr, 0) == 4
    assert find_min_index(arr, 2) == 4

def test_swap():
    arr = [1, 2, 3]
    swap(arr, 0, 2)
    assert arr == [3, 2, 1]
