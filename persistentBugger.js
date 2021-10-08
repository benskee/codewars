function persistence(num) {
    if (num < 10){
        return 0
    }
    else{
        let count = 1
        let addDigits = n =>{
            let sep = n.toString().split("")
            let t = 1
            for (x=0; x<sep.length; x++) {
                t = t * parseInt(sep[x])
            }
            return t
        } 

        let y = addDigits(num)

        while (y > 9) {
            count +=1
            y = addDigits(y)
        }
        return count
    }
}


console.log(persistence(39))
// , 3);
console.log(persistence(4))
// , 0);
console.log(persistence(25))
// , 2);
console.log(persistence(999))
// , 4);