var uniqueInOrder = function (iterable) {
    let previous = ''
    ans = []
    for (x=0; x<iterable.length; x++) {
        if (iterable[x] != previous) {
            previous = iterable[x]
            ans.push(iterable[x])
        }
    }
    return ans
}

console.log(uniqueInOrder('AAAABBBCCDAABBB'))
// , ['A', 'B', 'C', 'D', 'A', 'B'])