var countBits = function (n) {
    var a = n.toString(2)
    var ans = 0
    for (i = 0; i < a.length; i++) {
        if (a[i] === "1") {
            ans += 1
        }
    }
    return ans
};