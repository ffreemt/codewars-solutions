""" check unique solutions a^2 + b^2 + c^2.

N = 2

4, 7 => 1, 8
"""

from math import sqrt
from itertools import combinations_with_replacement

import logzero
from logzero import logger
logzero.loglevel(10)  # show logger.debug, default 20: show logger.info

BOUND = 3
BOUND = 10
N = 3

def main():
    """ main. """

for comb in combinations_with_replacement(range(1, BOUND + 1), N):
    # it0 = combinations_with_replacement(range(1, BOUND + 1), N)
    # comb = next(it0)

    a, b, c = comb
    sum_ = sum(map(lambda elm: elm*elm, comb))
    boundc = sqrt(sum_).__int__()

    for idxc in range(1, boundc + 1):
        boundb = sqrt(sum_ - idxc * idxc).__int__()
        for idxb in range(1, boundb + 1):
            bounda = sqrt(sum_ - idxc * idxc - idxb * idxb).__int__()
            for idxa in range(1, bounda + 1):
                sum0 = idxa * idxa + idxb * idxb + idxc * idxc
                if sum0 == sum_:
                    if set(comb) != {idxc, idxb, idxa}:
                        logger.info("comb: %s, idx: %s, %s, %s", comb, idxa, idxb, idxc)
                        break
