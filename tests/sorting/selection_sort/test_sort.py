# algorithms/selection_sort/tests/sort.py
from sorting.selection_sort.sort import selection_sort

def test_selection_sort():
    assert selection_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert selection_sort([]) == []
    assert selection_sort([5]) == [5]
