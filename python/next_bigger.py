""" https://www.codewars.com/kata/55983863da40caa2c900004e/train/python.

Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)
"""

from itertools import permutations
from more_itertools import peekable

'''
def next_bigger(n):
    """ Next bigger number with the same digits.

    >> next_bigger(12)
    21
    >>> next_bigger(513)
    531
    >>> next_bigger(2017)
    2071
    >>> next_bigger(414)
    441
    >>> next_bigger(144)
    414
    >>> next_bigger(452031452)  # 452031425
    452031524
    >>> next_bigger(82)  # 28
    -1

    >>>
    str_ = str(n)
    for len_ in range(2, len(str_) + 1):
        sorted_ = "".join(sorted(str_[-len_:], reverse=True))
        if not sorted_ == str_[-len_:]:
            res = str_[:-len_] + sorted_
            break
    else:
        res = -1

    return int(res)

    sorted_ = sorted(permutations(str(n)))
    sorted_ = sorted(list(set(sorted_)))
    idx = sorted_.index(tuple(str(n)))

    try:
        return int(''.join(sorted_[idx + 1]))
    except :
        return -1

    it_ = permutations(sorted(str(n)))
    prev = False
    for elm in it_:
        if prev and not elm == tuple(str(n)):
            res = "".join(elm)
            break
        if elm == tuple(str(n)):
            prev = True
    else:
        res = -1

    return int(res)  # works but still too slow
    """
'''

# def dict_order_next(seq):
_ = """
    >>> dict_order_next("144")
    '414'
    >>> dict_order_next(12)
    '21'
    >>> dict_order_next(513)
    '531'
    >>> dict_order_next(2017)
    '2071'
    >>> dict_order_next(414)
    '441'
    >>> dict_order_next(144)
    '414'
    >>> dict_order_next(82)  # 28
    -1
    >>> dict_order_next(5774)  # 7574
    '7457'
    >>> dict_order_next(14693425755774)  # '1469342575 7574'
    14693425757457

    """

# def next_permutation(case):
def next_bigger(case):
    """
    >>> next_bigger(82)
    -1
    >>> next_bigger(5774)
    7457
    >>> next_bigger(14693425755774)
    14693425757457

    """
    case = list(str(case))

    for index in range(1,len(case)):
        Px_index = len(case) - 1 - index
        #Start travelling from the end of the Data Structure
        Px = case[-index-1]
        Px_1 = case[-index]

        #Search for a pair where latter the is greater than prior
        if Px < Px_1 :
            suffix = case[-index:]
            pivot = Px
            minimum_greater_than_pivot_suffix_index = -1
            suffix_index=0

            #Find the index inside the suffix where ::: [minimum value is greater than the pivot]
            for Py in suffix:
                if pivot < Py:
                    if minimum_greater_than_pivot_suffix_index == -1 or   suffix[minimum_greater_than_pivot_suffix_index] >= Py:
                        minimum_greater_than_pivot_suffix_index=suffix_index
                suffix_index +=1
            #index in the main array
            minimum_greater_than_pivot_index = minimum_greater_than_pivot_suffix_index + Px_index +1

            #SWAP
            temp = case[minimum_greater_than_pivot_index]
            case[minimum_greater_than_pivot_index] = case[Px_index]
            case[Px_index] = temp

            #Sort suffix
            new_suffix = case[Px_index+1:]
            new_suffix.sort()

            #Build final Version
            new_prefix = case[:Px_index+1]
            next_permutation = new_prefix + new_suffix
            # return next_permutation
            return int("".join(next_permutation))
        elif index == (len(case) -1):
            #This means that this is at the highest possible lexicographic order
            # return False
            return -1
    # return True
    return -1

# %timeit next_bigger(14693425755774)  # 25 us


def next_bigger(n):
    """ codewars solution. """
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1;

    while True:
        i += 1;
        if sorted(str(i)) == ss and i != n:
            return i;

def next_bigger(n):
    str_n = str(n)
    ss = sorted(str_n)

    while n < int("".join(sorted(str_n, reverse=1))):
        n += 1;
        if sorted(str(n)) == ss:
            return n;

    return -1

# %timeit next_bigger(14693425755774)  # 38 ms

# 【吐槽】|l||l|ll||l||l|||ll|<longf@usc.edu> 12/7/2020 10:01:25 PM
def next_bigger(num):
    # turn num into array
    seq = [int(x) for x in str(num)]
    seq.reverse()
    # if seq only have one digital, skip
    if len(seq) <= 1:
        return -1
   
    left = 0
    right = -1
    v = seq[0]
    # scan the sequence
    for i, n in enumerate(seq):
        if n == v:
            continue
        # found descending right
        if n < v:
            right = i
            # search again previouse sequence for smallest choice
            for j, m in enumerate(seq[:right]):
                if seq[right] < m < seq[left]:
                    left = j
            break
           
        # update left
        left = i
        v = n
       
    # no descending part
    if right == -1:
        return -1
   
    # print(left, right)
   
    tmp = seq[right]
    seq[right] = seq[left]
    seq[left] = tmp
   
    # sort left part
    seq = sorted(seq[:right], reverse=True) + seq[right:]
    seq.reverse()
    return int(''.join(map(str, seq)))
    
%timeit next_bigger(14693425755774)  # 2 ms

# https://stackoverflow.com/questions/4223349/python-implementation-for-next-permutation-in-stl