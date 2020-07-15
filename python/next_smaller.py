"""
https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

https://stackoverflow.com/questions/59005190/find-next-smallest-number-with-same-digits-python

1 Starting from the right, find the first digit that has at least one smaller digit to its right. We'll call that digit X.
2 Then find the largest digit that is to the right of X, and is smaller than X. We'll call that digit Y.
3 Swap X and Y. This makes the number smaller.
4 Then sort all of the digits to the right of Y in descending order. This makes the number as big as possible, without making it bigger than the original.

For example:

1262347  // original number
  ^  ^
  X  Y

1242367  // after the swap
  ^  ^
  Y  X

1247632  // after sorting digits to the right of Y
  ^
  Y

"""
import logzero
from logzero import logger
logzero.loglevel(10)


def next_smaller1(n):
    """ next smaller

    timed out on codewars
    """
    str_n = str(n)
    ss = sorted(str_n)

    smallest = int("".join(sorted(str_n)))
    if n == smallest:
        return -1
    while n > smallest:
        n -= 1
        if sorted(str(n)) == ss:
            return n

def next_smaller(n):
    """ next smaller.

    n = 1262347
    xi = 2
    yi = 5
    """
    list_n = [*map(int, list(str(n)))]
    logger.debug("list_n: %s", list_n)

    # locate y
    len_ = len(list_n)
    for elm in range(0, len_ - 1):
        logger.debug("%s, %s", elm, len_ - 2 - elm)
        if list_n[len_ - 2 - elm] > list_n[len_ - 1 - elm]:
            xi = len_ - 2 - elm
            break
    else:
        return -1
    logger.debug(" xi: %s", xi)

    # locate yi
    max_ = max(filter(lambda elm: elm < list_n[xi], list_n[xi + 1:]))
    if max_ < list_n[xi]:
        yi = xi + 1 + list_n[xi + 1:].index(max_)
    else:
        return - 1

    logger.debug(" yi: %s", yi)

    # swap
    logger.debug(list_n)
    list_n[xi], list_n[yi] = list_n[yi], list_n[xi]
    logger.debug(list_n)

    # sort
    res = list_n[:xi + 1] + sorted(list_n[xi + 1:], reverse=True)

    res = int("".join(map(str, res)))

    # preceeding zero
    if len([*map(int, list(str(res)))]) < len(list_n):
        return -1

    if res == n:
        return -1

    return res

def test721():
    assert next_smaller(721) == 712
    assert next_smaller(10) == -1
    assert next_smaller(987654321) == 987654312

    # 10 -1
    #  should equal -1

def test_canary():
    assert next_smaller(1) == -1

def test0():
    assert next_smaller(1262347) == 1247632


def test_1():
    """
    Test.assert_equals(next_smaller(907), 790)
    Test.assert_equals(next_smaller(531), 513)
    Test.assert_equals(next_smaller(135), -1)
    Test.assert_equals(next_smaller(2071), 2017)
    Test.assert_equals(next_smaller(414), 144)
    Test.assert_equals(next_smaller(123456798), 123456789)
    Test.assert_equals(next_smaller(123456789), -1)
    Test.assert_equals(next_smaller(1234567908), 1234567890)
    """
    assert next_smaller(907) == 790
    assert next_smaller(531) == 513
    assert next_smaller(135) == -1
    assert next_smaller(2071) == 2017
    assert next_smaller(414) == 144


def test_2():
    assert next_smaller(123456798) == 123456789
    assert next_smaller(123456789) == -1
    assert next_smaller(1234567908) == 1234567890
