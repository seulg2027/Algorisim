'''
모든 지름길을 가는 경우의 수 -> BFS로 계산
'''

import sys
from collections import deque
input = sys.stdin.readline

n, d = map(int, input().split())
road = list(list(map(int, input().split())) for _ in range(n))
road = list(filter(lambda x: x[1] - x[0] > x[2] and x[1] <= d, road)) # 지름길이 아닌 건 필터링해주기
m = len(road)

start = list(map(list, zip(*road)))[0] if road else []

q = deque([(0, 0)]) # 목표 위치, 길이
answer = sys.maxsize

while q:
    now = q.popleft()
    
    if now[0] == d:
        answer = min(answer, now[1])
    elif now[0] in start:
        for i in range(m):
            if road[i][0] == now[0]:
                q.append((road[i][1], now[1]+road[i][2]))
    
    if now[0] < d:
        q.append((now[0]+1, now[1]+1))

print(answer)