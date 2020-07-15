""" https://www.codewars.com/kata/570409d3d80ec699af001bf9/train/python

1. fusc(0) = 0
2. fusc(1) = 1
3. fusc(2 * n) = fusc(n)
4. fusc(2 * n + 1) = fusc(n) + fusc(n + 1)
"""
def fusc(n):
    assert type(n) == int and n >= 0

    if n < 2:
        return n

    if n % 2 == 0:
        return fusc(n // 2)
    else:
        k = n // 2
        return fusc(k) + fusc(k + 1)

from functools import lru_cache

@lru_cache(maxsize=1024)
def fusc(n):
    assert type(n) == int and n >= 0

    if n < 2:
        return n

    if n % 2 == 0:
        return fusc(n // 2)
    else:
        k = n // 2
        return fusc(k) + fusc(k + 1)

# pt 2: reduce stack size
# https://www.codewars.com/kata/57040e445a726387a1001cf7/train/python
