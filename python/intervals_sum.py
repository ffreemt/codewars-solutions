"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

https://www.codewars.com/kata/52b7ed099cdc285c300001cd/solutions/python
interval sums

[
   [1,4],
   [7, 10],
   [3, 5]
]
Out[174]: [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]

Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
Test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
"""
import logzero
from logzero import logger
logzero.loglevel(10)
from functools import reduce


def sum_of_intervals1(intervals):
    """ sum_of_intervals.

    reduce(lambda acc, el: acc.update(set(range(el[0], el[1]))), intervals, set())

    reduce(lambda acc, el: not acc.update(set(range(el[0], el[1]))) and globals()['acc'], intervals, set())
    """

    _ = """if not intervals: return 0

    pool = []
    for elm in intervals:
        pool.extend(elm)
    min_ = min(pool)
    max_ = max(pool)

    # color intervals between min_ and max_ as -1
    color_bar = [0] * (max_ - min_ + 1)
    for elm in intervals:
        for idx in range(elm[0] + 1, elm[1] + 1):
            color_bar[idx - min_] = 1

    return sum(color_bar)
    # """
    _ = """
    set_ = set()
    for elm in intervals:
        for idx in range(elm[0] + 1, elm[1] + 1):
            set_.update({idx})
    return len(set_)
    # """

    # reduce(lambda acc, el: not acc.update(set(range(el[0], el[1]))) and globals()['acc'], intervals, set())

    return reduce(lambda acc, el: not acc.update(set(range(el[0], el[1]))) and globals()['acc'], intervals, set()).__len__()


from functools import reduce


def sum_of_intervals(intervals):
    return reduce(lambda acc, el: not acc.update(set(range(el[0], el[1]))) and locals()['acc'], intervals, set()).__len__()


"""
intervals = [ [ 1, 5 ], [ 6, 10 ] ]
intervals.reduce((acc, el, idx, arr) => {let start = el[0]; let range = el[1] - el[0]; while (range){ acc.add(start); start++; range--}; return acc}, new Set()).size

"""


def test1():
    """test1. """
    intervals = [
       [1, 4],
       [7, 10],
       [3, 5]
    ]
    assert sum_of_intervals(intervals) == 7


def test_sanity():
    """ test sanity. """
    assert not sum_of_intervals([])


def test2():
    """ test2. """
    assert sum_of_intervals([(1, 5)]) == 4
    assert sum_of_intervals([(1, 5), (6, 10)]) == 8
    assert sum_of_intervals([(1, 5), (1, 5)]) == 4
