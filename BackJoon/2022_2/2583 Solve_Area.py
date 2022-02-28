# 2583 영역 구하기

# bfs 문제 연습 ~

from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]

for _ in range(k):
  ay, ax, by, bx = map(int, input().split())
  for i in range(ax, bx):
    for j in range(ay, by):
      graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
result = []

def bfs_search(a, b):
  global cnt
  q = deque([(a, b)])
  visited[a][b] = 1
  square = 0
  while q:
    x, y = q.popleft()
    square += 1
    for i in range(4):
      rx = x + dx[i]
      ry = y + dy[i]
      if 0 <= rx < m and 0 <= ry < n and not visited[rx][ry] and graph[rx][ry] == 0:
        q.append((rx, ry))
        visited[rx][ry] = True
  result.append(square)
  cnt += 1

for i in range(m):
  for j in range(n):
    if not visited[i][j] and graph[i][j] == 0:
      bfs_search(i, j)

print(cnt)
result.sort()
for re in result:
  print(re, end=' ')