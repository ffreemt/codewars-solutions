"""
https://www.codewars.com/kata/55c04b4cc56a697bb0000048/solutions/python

scramble('rkqodlw', 'world'),  True
scramble('scriptjava', 'javascript'), True
scramble('katas', 'steak'), False

s1, s2 = 'scriptjava', 'javascript'
s1, s2 = 'katas', 'steak'

function scramble(s1, s2) {
    //let s1, s2;
    //s1 = 'katas'
    //s2 = 'steak'
    arr2 = Array.from(new Set(s2))

    let c1, c2;

    for (let i = 0; i < arr2.length {
        c1 = 0
        c2 = 0
        for (let idx = 0; idx < s1.length; idx++) {
            if (s1[idx] === arr2[i]) c1++
        }
        for (let idx = 0; idx < s1.length; idx++) {
            if (s1[idx] === arr2[i]) c2++
        }
        if (c2 > c1 ) return false;
    };

    return true;
}

// set2 = new Set(s2) // Array.from(set2)


"""
def scramble(s1, s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))
