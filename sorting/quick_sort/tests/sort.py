# algorithms/quick_sort/tests/sort.py
from algorithms.sorting.quick_sort.sort import quick_sort

def test_quick_sort():
    assert quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert quick_sort([]) == []
    assert quick_sort([5]) == [5]
