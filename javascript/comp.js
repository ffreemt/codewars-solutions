// https://www.codewars.com/kata/550498447451fbbd7600041c/train/javascript
// let a = [121, 144, 19, 161, 19, 144, 19, 11]

/*
# OK
a.reduce((acc, el) =>
  acc.hasOwnProperty(el) ? Object.assign(acc, {[el.toString()]: acc[el] + 1}) : Object.assign(acc, {[el.toString()]: 1}), {})

# same OK, must use .editor
a.reduce((acc, el) =>
  acc.hasOwnProperty(el) ? Object.assign(acc, {[el.toString()]: acc[el] + 1}) : Object.assign(acc, {[el.toString()]: 1}), {})

# OK qq-pal
a.reduce((acc, el) => {
  if (acc.hasOwnProperty(el))
    return Object.assign(acc, {[el.toString()]: acc[el] + 1});
return Object.assign(acc, {[el.toString()]: 1})}, {})
// */

// return !!a && !!b && JSON.stringify(a.reduce((acc, el) => acc.hasOwnProperty(el * el) ? Object.assign(acc, {[(el * el).toString()]: acc[el * el] + 1}) : Object.assign(acc, {[(el * el).toString()]: 1}), {})) === JSON.stringify(b.reduce((acc, el) => acc.hasOwnProperty(el) ? Object.assign(acc, {[el.toString()]: acc[el] + 1}) : Object.assign(acc, {[el.toString()]: 1}), {}))

// return !!a && !!b && JSON.stringify(a.reduce((acc, el) => acc.hasOwnProperty(el * el) ? Object.assign(acc, {[el * el]: acc[el * el] + 1}) : Object.assign(acc, {[el * el]: 1}), {})) === JSON.stringify(b.reduce((acc, el) => acc.hasOwnProperty(el) ? Object.assign(acc, {[el]: acc[el] + 1}) : Object.assign(acc, {[el]: 1}), {}))

// arr.reduce((acc, curr) => {
// acc[curr] = acc[curr] ? acc[curr] + 1 : 1;
// return acc;
// }, {});

/* // wrong solution
// 7 4 8 1
// 49+16==64+1

function comp(array1, array2){
  return !!array2 && !!array1 && array2.every( a=> array1.some( (b,i)=> a===b*b && delete array1[i] ) )
}
// */

// /*
function comp(a, b){
  return !!a && !!b && JSON.stringify(a.reduce((acc, el) => {acc[el * el] = acc[el * el] ? acc[el * el] + 1 : 1; return acc;}, {})) === JSON.stringify(b.reduce((acc, el) => {acc[el] = acc[el] ? acc[el] + 1 : 1; return acc;}, {}));
}
// */

module.exports = comp;