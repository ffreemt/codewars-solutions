"""
https://www.codewars.com/kata/584dee06fe9c9aef810001e8/train/python

Test.describe("Example tests")
Test.it("should work for some basic tests")
Test.assert_equals(green(1), 1)
Test.assert_equals(green(2), 5)
Test.assert_equals(green(3), 6)
Test.assert_equals(green(4), 25)
print("<COMPLETEDIN::>")
Test.it("should work for some bigger tests")
Test.assert_equals(green(12), 2890625)
Test.assert_equals(green(13), 7109376)
print("<COMPLETEDIN::>")
Test.it("should work for some advanced tests")
Test.assert_equals(green(100), 6188999442576576769103890995893380022607743740081787109376)
Test.assert_equals(green(110), 9580863811000557423423230896109004106619977392256259918212890625)
print("<COMPLETEDIN::>")
print("<COMPLETEDIN::>")

"""


def is_green(n):
    list_n = list(str(n))
    list_n2 = list(str(n * n))
    if list_n == list_n2[-len(list_n):]:
        return True
    return False


def green1(n):
    count = 0
    i = 1
    while count < n:
        if is_green(i):
            res = i
            count += 1
        i += 1
    return res


def green(n):
    if n == 1:
        return 1


def test5():
    assert green1(2) == 5


def test_long():
    assert green1(1) == 1
