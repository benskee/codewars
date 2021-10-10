function songDecoder(song) {
    let str = song.split("WUB").join(' ')
    let p = true
    let ans = ''
    for (x=0; x<str.length; x++) {
        if (str[x] == ' ') {
            if (p == false) {
                ans += ' '
                p = true
            }
        }
        else {
            ans += str[x]
            p = false
        }
    }
    return ans.trim()
}

console.log(songDecoder("AWUBBWUBC"))
// , "A B C", "WUB should be replaced by 1 space");
console.log(songDecoder("AWUBWUBWUBBWUBWUBWUBC"))
// , "A B C", "multiples WUB should be replaced by only 1 space");
console.log(songDecoder("WUBAWUBBWUBCWUB"))
// , "A B C", "heading or trailing spaces should be removed");