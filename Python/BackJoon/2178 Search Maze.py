# 미로 탐색

from collections import deque

n, m = map(int, input().split())
graph = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
  global n, m
  queue = deque()
  queue.append((0, 0))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if -1 < nx < n and -1 < ny < m:
        if graph[nx][ny] == 1:
          queue.append((nx, ny))
          graph[nx][ny] += graph[x][y]

for _ in range(n):
  graph.append(list(map(int, input())))

bfs()
print(graph[n-1][m-1])