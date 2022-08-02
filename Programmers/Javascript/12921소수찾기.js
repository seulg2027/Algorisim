
// 에라토스테네스의 체 풀이

function solution(n) {
    var isPrime = new Array(n+1).fill(true);
    
    for (var i=2; i < Math.sqrt(n); i++) {
        if (isPrime[i] === true){
            let j = 2;
            while ( i*j <= n ){
                isPrime[i*j] = false;
                j += 1
            }
        }
    }
    var answer = 0;
    for (var i=2; i < n+1; i++){
        if (isPrime[i] === true) {
            answer += 1;
        }
    }
    return answer;
}