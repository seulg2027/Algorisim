
// ㅎㅁㅎ 왜 레벨2지
function solution(n) {
    var answer = '';
    for (var i=1; i < n+1; i++) {
        if (i%2 === 0){ // 짝수라면
            answer += '박';
        } else {
            answer += '수';
        }
    }
    return answer;
}