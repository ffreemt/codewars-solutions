"""
https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python
"""
def solve(st):
    n = len(st)
    pre = []
    suf = []
    for elm in range(1, n):
        pre.append(st[:elm])
        suf.append(st[elm:])

    for elm in pre[::-1]:
        if elm in suf:
            if len(elm) < n // 2:
                return len(elm)
    return 0
