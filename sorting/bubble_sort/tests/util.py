# algorithms/bubble_sort/tests/util.py
from algorithms.bubble_sort.utils import swap

def test_swap():
    arr = [1, 2, 3]
    swap(arr, 0, 2)
    assert arr == [3, 2, 1]

    arr = [4, 5, 6]
    swap(arr, 1, 2)
    assert arr == [4, 6, 5]
