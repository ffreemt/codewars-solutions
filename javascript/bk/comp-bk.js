// https://www.codewars.com/kata/550498447451fbbd7600041c/train/javascript
// let a = [121, 144, 19, 161, 19, 144, 19, 11]
// let b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19];

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

module.exports = comp;
function comp(a, b){
  if (a === null || b === null)
    return false;

  if (a.length === 0 && b.length === 0)
    return true;
  colla = {};
  collb = {};

  // square and collect a
  a.forEach(el => {
    colla.hasOwnProperty(el * el) ? colla[el * el] += 1 : colla[el * el] = 1;
  });

  // collect b
  b.forEach(el => {
    collb.hasOwnProperty(el) ? collb[el] += 1 : collb[el] = 1;
  });

  let c = [];
  for (let el in colla) {
    c.push(colla[el] === collb[el]);
  }

  return c.every(el => el);

}