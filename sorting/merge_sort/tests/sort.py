# algorithms/merge_sort/tests/sort.py
from algorithms.merge_sort.sort import merge_sort

def test_merge_sort():
    assert merge_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert merge_sort([]) == []
    assert merge_sort([5]) == [5]
