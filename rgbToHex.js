function rgb(r, g, b) {
    ans = ''
    l = [r,g,b]
    const hexer = x => {
        if (x < 0) {
            x = 0
        }
        else if (x>255) {
            x = 255
        }

        const h = x.toString(16).toUpperCase()

        return x<16 ? "0"+h : h
    }
    l.map(n=> ans += hexer(n) )
    return ans
}

console.log(rgb(0, 0, 0))
// , '000000');
console.log(rgb(0, 0, -20))
// , '000000');
console.log(rgb(300, 255, 255))
// , 'FFFFFF');
console.log(rgb(173, 255, 47))
// , 'ADFF2F');