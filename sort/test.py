import pytest
import copy


input = [
    [2, 3, 5, 1, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 5, 4, 1],
    [3, 5 , 1],
    [2, 1],
    [1],
    []
]

expected = [sorted(x) for x in input]


def sort_wrapper (f):
    ic = copy.deepcopy(input)
    ec = copy.deepcopy(expected)
    for i, e in zip (ic, ec):
        got = f(i)
        print ("Input {} Got {} Expect {}".format(i, got, e))
        assert got ==  e

def test_insert_sort():
    from insert import insert_sort
    sort_wrapper(insert_sort)

def test_quick_sort ():
    from quick import quick_sort
    sort_wrapper(quick_sort)