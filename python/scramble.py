"""
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python

def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False

str1, str2 = 'katas', 'steak'

count "a" in str1 https://stackoverflow.com/questions/6120931/how-to-count-certain-elements-in-array
str1.split("").reduce((acc, el) => el === "a" ? acc + 1 : acc, 0)

str1.split("").filter(x => x=="a").length
"""

# pylint: disable=missing-docstring

from typing import List

from functools import reduce
from collections import Counter

_ = '''
def scramble(str1, str2):
    """ scramble.

    https://www.codewars.com/kata/55c04b4cc56a697bb0000048/python
    function scramble(str1, str2) {
  let occurences = str1.split("").reduce((arr, cur) => { arr[cur] ? arr[cur]++ : arr[cur] = 1; return arr; }, {});
  return str2.split("").every((character) => --occurences[character] >= 0);
}
    rewritten in python
    """

    # codewars js solution
    # occurences = reduce(lambda acc, el: not (acc.update({el: acc[el] + 1}) if acc.get(el) else acc.update({el: 1})) and locals()['acc'], str1, {})  # 13µs 17.2 µs

    # %timeit scramble('rkqodlw', 'world')  # 37 µs
    # occurences = counter(str1)

    # %timeit scramble('rkqodlw', 'world')  # 35 µs
    # oc = lambda str_: reduce(lambda acc, el: not(acc.update({el: str_.count(el)})) and locals()['acc'], set(str_), {})
    # occurences = oc(str1)

    # _ = map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2)

    # return all(_)
# '''

_ = """
from typing import List

def counter(str_: List[str]) -> dict:
    dict_ = {}
    for elm in set(str_):
        dict_.update({elm: str_.count(elm)})
    return dict_

def scramble(str1, str2):
    occurences = counter(str1)

    return all(map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2))

# %timeit scramble('rkqodlw', 'world')  # 35 µs
# """

_ = """
from functools import reduce

def scramble(str1, str2):
    occurences = reduce(lambda acc, el: not(acc.update({el: str1.count(el)})) and locals()['acc'], set(str1), {})

    return all(map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2))

# %timeit scramble('rkqodlw', 'world')  # 50 µs
# """

_ = """
from collections import Counter

def scramble(str1, str2):
    return not (Counter(str2) - Counter(str1))
# %timeit scramble('rkqodlw', 'world')  # 85 µs

# """

_ = """
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))
# %timeit scramble('rkqodlw', 'world')  # 16 µs
# """

# _ = """
def scramble(s1, s2):
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True
# %timeit scramble('rkqodlw', 'world')  # 11 µs
# """

def test_1():
    """ test_1. """
    assert scramble('rkqodlw', 'world')


def test_2():
    """ test_2. """
    assert scramble('cedewaraaossoqqyt', 'codewars')


def test_3():
    """ test_3. """
    assert not scramble('katas', 'steak')
