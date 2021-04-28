function solution(number){
    var ans=0
    var t=1
    while (t < number/3){
        if (t % 5 != 0){
            ans += t*3;
        }
        t++;
    }
    var t=1
    while (t < number/5){
        ans += t*5;
        t++;
    }
    return ans
}


console.log(solution(10))
// 23
