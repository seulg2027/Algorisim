function solution(answers) {
    var answer = [];
    var person1_len = Math.floor(answers.length / 5) ? Math.floor(answers.length / 5) + 1 : 1;
    var person2_len = Math.floor(answers.length / 8) ? Math.floor(answers.length / 8) + 1 : 1;
    var person3_len = Math.floor(answers.length / 10) ? Math.floor(answers.length / 10) + 1 : 1;
    var person1 = [], person2 = [], person3 = [];
    var person1_ = [1, 2, 3, 4, 5];
    var person2_ = [2, 1, 2, 3, 2, 4, 2, 5];
    var person3_ = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    // 정답 추가
    for (let i=0; i < person1_len; i++) {
        person1.push(...person1_);
    }
    for (let i=0; i < person2_len; i++) {
        person2.push(...person2_);
    }
    for (let i=0; i < person3_len; i++) {
        person3.push(...person3_);
    }
    var cnts = [0, 0, 0];
    
    // 정답 맞은 수 만큼
    for (let i=0; i < answers.length; i++) {
        if (person1[i] === answers[i]) {
            cnts[0] += 1
        }
        if (person2[i] === answers[i]) {
            cnts[1] += 1
        }
        if (person3[i] === answers[i]) {
            cnts[2] += 1
        }
    }
    
    var max_value = -1;
    var max_person = 0;
    for (var c=0; c < 3; c++) {
        if (cnts[c] === 0) { // 예외처리 => 하나도 정답이 없을 경우
            continue;
        }
        if (cnts[c] > max_value) {
            max_value = cnts[c];
            max_person = c;
            answer = [];
            answer.push(max_person+1);
        } else if (cnts[c] === max_value) {
            max_person = c;
            max_value = cnts[c];
            answer.push(max_person+1);
        }
    }
    
    return answer;
}