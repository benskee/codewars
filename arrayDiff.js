function arrayDiff(a, b) {
    var ans = a.filter(function(x) { return b.indexOf(x) == -1})
    return ans
}



console.log(arrayDiff([], [4, 5]))
//  "a was [], b was [4,5]");
console.log(arrayDiff([3, 4], [3]))
//  "a was [3,4], b was [3]");
console.log(arrayDiff([1, 8, 2], []))
//  "a was [1,8,2], b was []");
console.log(arrayDiff([1, 2, 3], [1, 2]))
//  "a was [1,2,3], b was [1,2]");