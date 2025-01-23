# algorithms/bubble_sort/tests/sort.py
from algorithms.sorting.bubble_sort.sort import bubble_sort

def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
