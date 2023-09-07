'''
42587번 프로세스
구현~,, 테케를 잘 넣어보자
'''

from collections import deque

def solution(priorities, location):
    q = deque([])
    answer = 0
    
    for j in range(len(priorities)):
        q.append((priorities[j], j))
    
    while q:
        prior, now = q.popleft()
        execute = 1
        for i in priorities: # 대기 중인 프로세스 확인
            if prior < i:
                q.append((prior, now))
                execute = 0
                break # 해당 턴 종료
        if execute == 1: # 다시 큐에 넣지 않고 실행한다면
            answer += 1 # 실행순서 더하기
            priorities.remove(prior) # 대기 중인 프로세스에서 제거
            if location == now: # 주어진 프로세스와 같다면
                break
    
    return answer