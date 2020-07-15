"""
https://www.codewars.com/kata/5a3dd29055519e23ec000074/train/python

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

If the score < 0, return 0.

Test.assert_equals(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
Test.assert_equals(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
Test.assert_equals(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
Test.assert_equals(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)
"""


def check_exam(arr1, arr2):
    score = 0
    for idx, elm in enumerate(arr2):
        if elm in [""]:
            continue
        elif elm in [arr1[idx]]:
            score += 4
        else:
            score -= 1
    if score < 0:
        score = 0

    return score


def test2():
    arr1, arr2 = ["a", "a", "c", "b"], ["a", "a", "b",  ""]
    assert check_exam(arr1, arr2) == 7
