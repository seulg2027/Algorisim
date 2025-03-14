'''
14940번 쉬운 최단거리

도달할 수 없으면 -1,, 이거 예외케이스 생각해야함
처음부터 예외케이스 모두 적어두는 습관 기르기
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
map_list = list(list(map(int, input().split())) for _ in range(N))
visited = list([False] * M for _ in range(N))
ans = list([-1] * M for _ in range(N)) # 도달할 수 없는 위치는 -1로 나타냄
q = deque([])

for i in range(N):
    for j in range(M):
        if map_list[i][j] == 2: # 목표지점이면 넣기
            q.append((i, j, 0))
            visited[i][j] = True
            ans[i][j] = 0
        elif map_list[i][j] == 0: # 갈 수 없는 땅이면 모두 0
            ans[i][j] = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while q:
    x, y, cnt = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if map_list[nx][ny] == 1:
                q.append((nx, ny, cnt+1))
                ans[nx][ny] = cnt+1
                visited[nx][ny] = True

for a in ans:
    print(*a)