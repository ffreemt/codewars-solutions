"""

https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/javascript
function findOutlier(integers){
  return integers.filter(el => Math.abs(el) % 2).length === 1 ? integers.filter(el => el % 2)[0] : integers.filter(el => Math.abs(el) % 2 === 0)[0]
}

integers = [2, 4, 0, 100, 4, 11, 2602, 36]
integers = [160, 3, 1719, 19, 11, 13, -21]

return integers.filter(el => Math.abs(el) % 2).length === 1 ? integers.filter(el => el % 2)[0] : integers.filter(el => Math.abs(el) % 2 - 1)[0]

return integers.filter(el => Math.abs(el) % 2).length === 1 ? integers.filter(el => el % 2)[0] : integers.filter(el => Math.abs(el) % 2 === 0)[0]

"""
from collections import reduce

def find_outlier(integers):
    ''' parity outlier. '''
    lst = [*map(lambda elm: elm % 2, integers)]

    # is_odd = 1 if sum(lst) < 2 else 0

    if 1 if sum(lst) < 2 else 0:  # is_odd true
      pos = lst.index(1)
    else:
      pos = lst.index(0)

    return integers[pos]


def find_outlier(integers):
    """ parity outlier.

    """
    odd = [*filter(lambda elm: elm % 2, integers)]
    if len(odd) == 1:
        return odd[0]

    return [*filter(lambda elm: elm % 2 - 1, integers)][0]

