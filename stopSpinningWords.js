function spinWords(string){
    const words = string.split(' ');
    var ans = ""
    for (var i = 0; i < words.length; i++) {
        if (words[i].length > 4) {
            ans += " " + words[i].split("").reverse().join("");
        }
        else {
            ans += " " + words[i];
        }
    }
    return ans.substring(1, ans.length);
    
}



console.log(spinWords("Welcome"))
// , "emocleW");
console.log(spinWords("Hey fellow warriors"))
// , "Hey wollef sroirraw");
console.log(spinWords("This is a test"))
// , "This is a test");
console.log(spinWords("This is another test"))
// , "This is rehtona test");
console.log(spinWords("You are almost to the last test"))
// , "You are tsomla to the last test");
console.log(spinWords("Just kidding there is still one more"))
// , "Just gniddik ereht is llits one more");
console.log(spinWords("Seriously this is the last one"))
// , "ylsuoireS this is the last one");