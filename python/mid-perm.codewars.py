"""https://www.codewars.com/kata/simple-fun-number-159-middle-permutation/train/python

https://gist.github.com/Hutdris/bd377d183e8e3983e4549a9fa4304115

"""
from itertools import permutations

def fact(n):
    return 1 if n < 1 else n * fact(n - 1)

_ = """
def middle_permutation(string):
    pos = fact(len(string)) // 2
    it = permutations(sorted(string))
    for elm in range(pos):
        _ = next(it)
    return "".join(_)
# """
_ = '''
from itertools import permutations

def middle_permutation(string):
  """
  Get the middle permutation of a sorted
  list of possible string permutations.
  """
  perms = [''.join(perm) for perm in
           permutations("".join(sorted(string)))]
  # perms.sort()
  mid = len(perms)/2

  if len(perms) % 2:
      return perms[int(mid+0.5)]
  else:
      return perms[int(mid)-1]
  # '''

MAX_N = 20

factorail_table = dict()
factorail_table[0] = 1
for i in range(1, MAX_N):
    factorail_table[i] = factorail_table[i-1] * i

def perm(ith, s):
    if factorail_table[len(s)] <= ith or ith < 0:
        raise ValueError
    elif len(s) == 1:
        return s
    else:
        sub_seq_len = factorail_table[len(s)-1]
        head_idx = ith // sub_seq_len
        next_ith = ith % sub_seq_len
        head = s[head_idx]
        next_s = ''.join(s.split(s[head_idx]))
        return head + perm(next_ith, next_s)

def middle_permutation(string):
    pos = fact(len(string)) // 2 - 1
    return perm(pos, string)
