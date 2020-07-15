""" https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python
"""
from itertools import permutations


def middle_permutation1(string):
    """
    Get the middle permutation of a sorted
    list of possible string permutations.

    timed out in codewars
    """
    perms = ["".join(perm) for perm in permutations(string)]
    perms.sort()
    mid = len(perms) / 2

    if len(perms) % 2:
        return perms[int(mid + 0.5)]
    else:
        return perms[int(mid) - 1]


def next_permutation(seq):
    """
    >>> next_permutation(231)
    '213'

    """
    if isinstance(seq, int):
        seq = "".join(map(str, list(seq)))
