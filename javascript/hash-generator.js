function generateHashtag (str) {
  if (!str.trim().length) return false;

  let a = str.trim().split(" ");

  let res = "#" + a.map(el => el ? el[0].toUpperCase() + el.slice(1) : el).join("");
  if (res.length > 140) return false;

  return res;
}

let str = "code" + " ".repeat(140) + "wars";
console.log(generateHashtag (str));
