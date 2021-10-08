function findOutlier(integers) {
    var e = 0
    var o = 0
    for (var x = 0; x<3; x++) {
        if (Math.abs(integers[x]) % 2 != 1){
            e++
        }
        else {
            o++
        }
    }
    if (e > o) {
        return integers.filter(e => Math.abs(e % 2) == 1)[0]
    }
    else {
        return integers.filter(e => Math.abs(e % 2) != 1)[0]
    }
}




console.log(findOutlier([0, 1, 2]))
// , 1)
console.log(findOutlier([1, 2, 3]))
// , 2)
console.log(findOutlier([2,6,8,10,3]))
// , 3)
console.log(findOutlier([0,0,3,0,0]))
// , 3)
console.log(findOutlier([1,1,0,1,1]))
// , 0)
console.log(findOutlier([152972567, -93084899, -37252185, 153643049, -70719855, -1870093, -102288773, 26661383, -187321507, 24797397, -83133447, -142809865, 6166845, -4300025, 142512853, 42294561, 179957664]))
// , 179957664)