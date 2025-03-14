'''
16174번 점프왕 쩰리(large)

기본적인 BFS 문제
'''

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = list(list(map(int, input().split())) for _ in range(N))
visited = list([False] * N for _ in range(N)) # 방문 여부 체크해야 쓸데없는 반복문을 안 돌 수가 있음
res = False

dx = [1, 0]
dy = [0, 1]

q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    if graph[x][y] == -1:
        res = True
        break
    
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))

print("HaruHaru" if res else "Hing")