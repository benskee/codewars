function isValidWalk(walk) {
    if (walk.length != 10) {
        return false
    }
    const count = (l, w=walk) => {
        return w.filter(x => x == l).length
    }
    if (count('n') == count('s') && count('e') == count('w')) {
        return true
    }
    return false
}

console.log(isValidWalk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
// , 'should return true');
console.log(isValidWalk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
// , 'should return false');
console.log(isValidWalk(['w']))
// , 'should return false');
console.log(isValidWalk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
// , 'should return false');