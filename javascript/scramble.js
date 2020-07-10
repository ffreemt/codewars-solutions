/*
function scramble(str1, str2) {
  let occurences = str1.split("").reduce((arr, cur) => { arr[cur] ? arr[cur]++ : arr[cur] = 1; return arr; }, {});
  return str2.split("").every((character) => --occurences[character] >= 0);
}

python reduce lambda:

str1 = 'katas'
str2 = 'steak'

occurences = reduce(lambda acc, el: not (acc.update({el: acc[el] + 1}) if acc.get(el) else acc.update({el: 1})) and locals()['acc'], str1, {})
# [*map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2)]

all(map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2))

https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python
from functools import reduce

def scramble(str1, str2):
    occurences = reduce(lambda acc, el: not (acc.update({el: acc[el] + 1}) if acc.get(el) else acc.update({el: 1})) and locals()['acc'], str1, {})
    return all(map(lambda el: not (occurences.update({el: occurences[el] - 1}) if occurences.get(el) else occurences.update({el: -1})) and (occurences[el] > -1), str2))

// */

function scramble(s1, s2) {
  //let s1, s2;
  //s1 = 'katas'
  //s2 = 'steak'
  // Counter:
  // s2.split("").reduce((acc, el) => { acc[el] ? acc[el]++ : acc[el] = 1; return acc}, {});

  let arr2 = Array.from(new Set(s2));

  let c1, c2;

  for (let i = 0; i < arr2.length; i++) {
    c1 = 0;
    c2 = 0;
    for (let idx = 0; idx < s1.length; idx++) {
      if (s1[idx] === arr2[i]) c1++;
    }
    for (let idx = 0; idx < s1.length; idx++) {
      if (s2[idx] === arr2[i]) c2++;
    }
    if (c2 > c1 ) return false;
  }

  return true;
}

module.exports = scramble;