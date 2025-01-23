# algorithms/quick_sort/tests/util.py
from algorithms.sorting.quick_sort.util import partition

def test_partition():
    arr = [5, 3, 8, 6, 2, 7, 4, 1]
    left, middle, right = partition(arr, 5)
    assert left == [3, 2, 4, 1]
    assert middle == [5]
    assert right == [8, 6, 7]
