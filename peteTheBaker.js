function cakes(r, a) {
    let min = [] 
    Object.keys(r).forEach(x => {
        let y = Math.floor(a[x] / r[x])
        y ? min.push(y) : min.push(0)
    })
    if (min.length == 0) {return 0}
    return Math.min(...min)
}




console.log(cakes({ flour: 500, sugar: 200, eggs: 1 }, { flour: 1200, sugar: 1200, eggs: 5, milk: 200 }))
// , 2, 

console.log(cakes({ apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100 }, { sugar: 500, flour: 2000, milk: 2000 }))
// , 0