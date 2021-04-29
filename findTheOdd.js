function findOdd(A) {
    var setA = [...new Set(A)];
    for (i = 0; i < setA.length; i++) {
        if (A.filter(x => x === setA[i]).length % 2 === 1 ) {
                return setA[i]
        }
    }
}
        


console.log(findOdd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]));
// , 5);
console.log(findOdd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]));
// , -1);
console.log(findOdd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]));
// , 5);
console.log(findOdd([10]));
// , 10);
console.log(findOdd([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]));
// , 10);
console.log(findOdd([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]));
// , 1);