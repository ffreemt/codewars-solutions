a, b = "abcxyz", "ayxz"

from collections import Counter

def solve(a,b):
    a_ = Counter(a)
    b_ = Counter(b)

    for elm, val in b_.items():
        if val >= a_[elm]:
            return 0

    buff = 0
    for elm, val in a_.items():
        buff += val - b_[elm]
    return buff


solve("abcxyz","ayxz") == 2
