function duplicateEncode(word) {
    let ans = ''
    let w = word.toLowerCase()
    for (let l=0; l<w.length; l++) {
        if (w.split(w[l]).length-1 > 1) {
            ans += ")"
        }
        else {
            ans += "("
        }
    }
    return ans
}


console.log(duplicateEncode("din"))
// , "(((");
console.log(duplicateEncode("recede"))
// , "()()()");
console.log(duplicateEncode("Success"))
// , ")())())", "should ignore case");
console.log(duplicateEncode("(( @"))
// , "))((");