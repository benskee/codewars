function firstNonRepeatingLetter(s) {
    for (x=0; x<s.length; x++) {
        s1 = s.toLowerCase()
        if (s1.indexOf(s1[x]) == s1.lastIndexOf(s1[x])) {
            return s[x]
        }
    }
    return ""
}


console.log(firstNonRepeatingLetter('a'))
// , 'a');
console.log(firstNonRepeatingLetter('stress'))
// , 't');
console.log(firstNonRepeatingLetter('moonmen'))
// , 'e');