# algorithms/insertion_sort/tests/util.py
from algorithms.sorting.insertion_sort.util import shift_right

def test_shift_right():
    arr = [4, 3, 2, 1]
    shift_right(arr, 2, 1)
    assert arr == [4, 3, 3, 2]
