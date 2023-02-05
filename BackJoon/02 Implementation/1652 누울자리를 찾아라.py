'''
1652번 누울 자리를 찾아라
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited_x = [[0] * n for _ in range(n)]
visited_y = [[0] * n for _ in range(n)]
ans = [0, 0]

def is_sleepedx(x, y):
    a = 0
    q = deque([[x, y]])
    visited_x[x][y] = 1
    while q:
        now = q.popleft()
        a += 1
        nx = now[0] + 1
        if 0 <= nx < n and 0 <= y < n and not visited_x[nx][y]:
            if graph[nx][y] == '.':
                q.append([nx, y])
                visited_x[nx][y] = 1
    if a > 1:
        ans[0] += 1

def is_sleepedy(x, y):
    a = 0
    q = deque([[x, y]])
    visited_y[x][y] = 1
    while q:
        now = q.popleft()
        a += 1
        ny = now[1] + 1
        if 0 <= x < n and 0 <= ny < n and not visited_y[x][ny]:
            if graph[x][ny] == '.':
                q.append([x, ny])
                visited_y[x][ny] = 1
    if a > 1:
        ans[1] += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == '.':
            is_sleepedy(i, j)

for i in range(n):
    for j in range(n):
        if graph[j][i] == '.':
            is_sleepedx(j, i)

print(ans[1], ans[0])