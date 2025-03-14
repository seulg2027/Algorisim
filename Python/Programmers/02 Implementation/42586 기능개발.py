'''
42586번 기능개발 풀이
'''

import math

def solution(progresses, speeds):
    answer = []
    works = []
    n = len(progresses)
    cnt = 1
    
    # 작업 배포일 계산
    for i in range(n):
        sec = int(math.ceil((100 - progresses[i]) / speeds[i]))
        if i != 0: # 첫 작업이 아니면 이전 작업과 비교
            if works[i-1] >= sec: # 이전 작업이 더 오래 걸리는 경우
                sec = works[i-1]
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1
        works.append(sec)
        
        if i == n-1:
            answer.append(cnt)
    
    return answer

