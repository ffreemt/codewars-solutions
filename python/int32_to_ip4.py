"""
https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/train/python
"""


def int32_to_ip(int32):
    ip4 = []
    quo = int32
    for elm in range(4):
        quo, rem = divmod(quo, 256)
        ip4.append(str(rem))

    return ".".join(ip4[::-1])


def test1():
    assert int32_to_ip(2154959208) == "128.114.17.104"


def test2():
    assert int32_to_ip(0) == "0.0.0.0"


def test3():
    assert int32_to_ip(2149583361) == "128.32.10.1"