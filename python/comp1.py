""" Are they the "same"?


证明：两组 n （n>1) 个非零整数平方的和相等时，两组n个非零整数各自相等。

n=2
给定: x, y, a, b 正整数.
假定: x <= y, and a <= b (否则可交换x 和 y， 或 a 和 b)

x^2 +y^2 = a^2 + b^2
=> x = a, y = b （根据勾股定理，斜边长度固定后，其他两边长度固定。不知道是不是有点勉强）

n=3：根据勾股定理可简化成 n=2。

根据归纳法结论成立。
q.e.d. XXX

https://www.codewars.com/kata/reviews/5556c27101231dd24f00031a/groups/5acdeab9ba4a65529e0000b7
function comp(array1, array2){
  return Array.isArray(array1) && Array.isArray(array2) &&
         array1.length == array2.length && array1.reduce((acc,v)=>acc+v*v,0) == array2.reduce((acc,v)=>acc+v,0);
}

The test cases should include：assert(!comp([7, 4], [64, 1])

I notice the solution at https://www.codewars.com/kata/reviews/5556c27101231dd24f00031a/groups/5acdeab9ba4a65529e0000b7 (function comp(array1, array2){
  return Array.isArray(array1) && Array.isArray(array2) &&
         array1.length == array2.length && array1.reduce((acc,v)=>acc+v*v,0) == array2.reduce((acc,v)=>acc+v,0);
}) will fail assert(!comp([7, 4], [64, 1]) but still accepted as a solutioin.

"""

from typing import List


def comp(array1: List[int], array2: List[int]) -> bool:
    """ Are they the "same"? """

    if not array1:
        return False
    if not array2:
        return False

    # pylint: disable=unneeded-not
    # numb1, numb2: array1 array2 里非零整数的个数
    numb1 = sum(map(lambda elm: not not elm, array1))
    numb2 = sum(map(lambda elm: not not elm, array2))
    if not numb1 == numb2:
        return False

    return sum(map(lambda elm: elm * elm, array1)) == sum(array2)


def test_empty1():
    """ test_empty1. """
    array1 = []
    array2 = [1, ]
    assert not comp(array1, array2)


def test_empty2():
    """ test_empty2. """
    array2 = []
    array1 = [1, ]
    assert not comp(array1, array2)


# pylint: disable=invalid-name
def test_a1a2():
    """ test_a1a2. """
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]  # noqa
    assert comp(a1, a2)


def test_a1_a2():
    """ test_a1_a2. """
    a1_ = [120, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]  # noqa
    assert not comp(a1_, a2)
