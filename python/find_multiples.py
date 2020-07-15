"""
https://www.codewars.com/kata/58ca658cc0d6401f2700045f/train/python

Test.assert_equals(find_multiples(5, 25), [5, 10, 15, 20, 25])
Test.assert_equals(find_multiples(1, 2), [1, 2])
"""

def find_multiples(integer, limit):
    """ find multiples.

    >>> find_multiples(5, 25)
    [5, 10, 15, 20, 25]
    >>> find_multiples(1, 2)
    [1, 2]
    """

    return [*filter(lambda elm: not (elm % integer) , range(integer, limit + 1))]
