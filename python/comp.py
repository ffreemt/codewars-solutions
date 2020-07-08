'''
Are they the "same"?
    https://www.codewars.com/kata/550498447451fbbd7600041c/solutions/javascript

    function comp(array1, array2){
      # return !!array2 && !!array1 && array2.every( a=> array1.some( (b,i)=> a===b*b && delete array1[i] ) )
      return !!array2 && !!array1 && array2.every( a=> array1.some( (b,i)=> a===b*b && Object.assign(array1, {[i]: 0} ) ) )
    }

    function comp(array1, array2){
      return Array.isArray(array1) && Array.isArray(array2) &&
             array1.length == array2.length && array1.reduce((acc,v)=>acc+v*v,0) == array2.reduce((acc,v)=>acc+v,0);
    }

    https://www.codewars.com/users/clandestino
    function comp(array1, array2){
      return !!array2 && !!array1 && array1.reduce((acc, el)=>acc+el*el,0) == array2.reduce((acc,el)=>acc+el,0);
    }

    """
    _ = """
    if not array1:
        return True
    if not array2:
        return True

    for a in array2:
        _ = False
        for i, b in enumerate(array1):
            if a == b * b:
                _ = True
                # del array1[i]
                array1[i] = 0
                break
        if not _:
            return False
    return True
    // """
'''

# pylint: disable=invalid-name

from typing import List


def comp(array1: List[int], array2: List[int]) -> bool:
    """ Are they the "same"? """
    return not not array1 and not not array1 and sum(map(lambda elm: elm * elm, array1)) == sum(array2)


def test_empty1():
    """ test_empty1. """
    array1 = []
    array2 = [1, ]
    assert comp(array1, array2)


def test_empty2():
    """ test_empty2. """
    array2 = []
    array1 = [1, ]
    assert comp(array1, array2)


def test_a1a2():
    """ test_a1a2. """
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(a1, a2)


def test_a1_a2():
    """ test_a1_a2. """
    a1_ = [120, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert not comp(a1_, a2)
