function comp(array1, array2) {
    arr1 = array1.map(x => x*x).sort((a,b)=>(a-b))
    arr2 = array2.sort((a, b) => (a - b))

    return JSON.stringify(arr1) == JSON.stringify(arr2)
}
a1 = [121, 144, 19, 161, 19, 144, 19, 11];
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19];

console.log(comp(a1,a2))