'''
152995번 인사고과

아이디어가 중요

인센티브를 못받는 사람을 가려내야함
N이 100,000 이니 O(NlogN)만 가능 -> "최댓값"을 이용하여 인센티브 가려내기
'''


def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a+target_b
    
    # 근무태도점수:내림차순, 동료평가점수:오름차순
    # 단 하나라도 모두 낮은 점수가 한번이라도 있다면 인센티브를 지급하지 않기 때문
    # [3,2],[3,2],[2,1],[2,2],[1,4]
    scores.sort(key=lambda x:(-x[0], x[1]))
    max_b = 0
    
    for i in range(len(scores)):
        if scores[i][0] > target_a and scores[i][1] > target_b:
            return -1
        
        if max_b <= scores[i][1]:
            max_b = scores[i][1]
            # 완호보다 높은 점수일 경우
            if scores[i][0]+scores[i][1] > target_score:
                answer += 1
    
    return answer+1