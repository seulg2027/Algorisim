'''
42627번 디스크 컨트롤러

heapq 사용하는 문제

예외가 너무 많아서 힘들었다ㅠㅠ
꼼꼼히 보기!
'''

import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    # total 최대 500 * 2,000 = 1,000,000 이므로 괜찮음
    total = sum(map(lambda x: x[0] + x[1], jobs)) # 최대 시간을 구해야함ㅠ 케이스가 많아서 딱 맞는 시간을 구하기가 쉽지 않음
    time = 0
    now = []
    q = []
    res = []
    
    # 시간이 더해지면서 시간당으로 살펴보는 방식
    while time <= total:
        # [0, 1], [0, 2]와 같이 동일한 시간에 들어오는 job을 고려해서 반목문으로 설계
        while jobs:
            if jobs[0][0] == time:
                process = jobs.pop(0)
                heapq.heappush(q, (process[1], process[0]))
            else:
                break
        
        # 현재 작업하고 있는 Job이 없다면
        if not now or now[0] == 0:
            if now:
                res.append(time - now[1])
                now = []
            
            if not q and jobs: # q는 비었는데 job이 남아있다면 시간만 흘러가게 하기
                time += 1
                continue
            elif not q and not jobs: # q와 job이 모두 비었다면 멈춰 -> 시간이 남았더라도 중간에 작업 종료 선언 가능
                break
            else:
                p = heapq.heappop(q)
                now = []
                now.append(p[0]-1)
                now.append(p[1])
        # Job이 있다면 시간 빼주기
        else:
            now[0] = now[0] - 1
        
        time += 1
    
    answer = sum(res) // len(res)
    
    return answer