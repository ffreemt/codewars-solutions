https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

"apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    "apples, pears\ngrapes\nbananas"
"a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd"

string = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]

string = "strawberries\noranges lemons '\noranges apples bananas strawberries avocados pears\navocados apples avocados\ncherries strawberries oranges , strawberries"
markers = ['^', '.', "'", '#', '!', '-', '?']
exp = 'strawberries\noranges lemons\noranges apples bananas strawberries avocados pears\navocados apples avocados\ncherries strawberries oranges , strawberries'

lines = string.splitlines()
patt = re.compile(rf"[{''.join(markers)}]")

map(patt.split, lines)

"\n".join(map(lambda elm: patt.split(elm)[0].strip(), lines))

import re

def solution(string, markers):
    if not markers:
        return string
    lines = string.splitlines()
    patt = re.compile(rf"[{''.join(markers)}]")

    return "\n".join(map(lambda elm: patt.split(elm)[0].strip(), lines))