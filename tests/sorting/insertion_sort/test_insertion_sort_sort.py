# algorithms/insertion_sort/tests/sort.py
from sorting.insertion_sort.sort import insertion_sort

def test_insertion_sort():
    assert insertion_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert insertion_sort([]) == []
    assert insertion_sort([5]) == [5]
