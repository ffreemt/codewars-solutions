"""
https://www.codewars.com/kata/526989a41034285187000de4/train/python
"""

def ips_between(start, end):
    st = map(int, start.split("."))
    en = map(int, end.split("."))

    return sum([el * 256 ** (3 - idx) for idx, el in enumerate(en)]) - sum([el * 256 ** (3 - idx) for idx, el in enumerate(st)])


def test1():
    assert ips_between("10.0.0.0", "10.0.0.50") == 50


def test2():
    assert ips_between("20.0.0.10", "20.0.1.0") == 246
