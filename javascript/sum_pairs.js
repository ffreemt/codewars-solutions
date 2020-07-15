// https://www.codewars.com/kata/54d81488b981293527000c8f/train/javascript

// https://nealbuerger.com/2018/02/codewars-sum-of-pairs/
/*
// [10, 5, 2, 3, 7, 5], 10
// [10, 5, 5, 2, 3, 7], 10
var sum_pairs = function (arr, sum) {
    let viewedValues = []
    for (let i = 0; i < arr.length; i++) {
        let currentValue = arr[i];
        let difference = sum - currentValue;
        if (viewedValues[difference]) {
            let result = [difference, currentValue];
            return result;
        }
        viewedValues[currentValue] = true;
    }
    return undefined;
}
*/

/* // https://stackoverflow.com/questions/42270462/optimizing-solution-of-sum-of-pairs-codewars



var sum_pairs=function(ints, s){
  if (ints.length < 2) return undefined; //not enough numbers for pair.
  let intSet = new Set()
  intSet.add(ints[0]);
  for (let i=1; i < ints.length; ++i){
    let needed = s-ints[i];
    if (intSet.has(needed)){//check if we have already seen the number needed to complete the pair.
      return [needed,ints[i]];
    }
    intSet.add(ints[i]);//if not insert the number in set and continue.
  }
  return undefined;//No answer found
}

*/


// var sum_pairs=function(ints, s){
function sum_pairs(ints, s){
  let store = new Set(), cand;
  for (const e of ints){
    cand = s - e;
    if (store.has(cand)) return [cand, e];
    store.add(e);
  }
  return undefined;
}


// console.log(sum_pairs([1, 4, 8, 7, 3, 15], 8))
// console.log(sum_pairs([1, -2, 3, 0, -6, 1], -6))
// console.log(sum_pairs([0, 2, 0], 0));
//
// console.log(sum_pairs([10, 5, 2, 3, 7, 5], 10));

module.exports = sum_pairs;
