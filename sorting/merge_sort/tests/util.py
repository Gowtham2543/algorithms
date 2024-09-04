# algorithms/merge_sort/tests/util.py
from algorithms.merge_sort.utils import merge

def test_merge():
    arr = [0] * 6
    L = [1, 3, 5]
    R = [2, 4, 6]
    merge(arr, L, R)
    assert arr == [1, 2, 3, 4, 5, 6]
