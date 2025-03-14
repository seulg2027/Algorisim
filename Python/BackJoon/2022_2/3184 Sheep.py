# 3184 양

# bfs 문제

from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
visited = [[0] * c for _ in range(r)]
graph = []
for _ in range(r):
  graph += [list(map(str, input().rstrip()))]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wolves = 0
sheeps = 0

def bfs(a, b):
  global r, c, wolves, sheeps
  wolf = 0
  sheep = 0
  q = deque([(a, b)])
  while q:
    x, y = q.popleft()
    if not visited[x][y]:
      if graph[x][y] == 'v':
        wolf += 1
      elif graph[x][y] == 'o':
        sheep += 1
    else:
      continue # 두 번 넣었다면 밑에 코드 실행시키지말고 무시
    visited[x][y] = 1
    for i in range(4):
      rx = x + dx[i]
      ry = y + dy[i]
      if 0 < rx < r and 0 < ry < c and graph[rx][ry] != '#' and not visited[rx][ry]:
        q.append((rx, ry))
  if wolf >= sheep:
    wolves += wolf
  elif wolf < sheep:
    sheeps += sheep

for i in range(r):
  for j in range(c):
    if not visited[i][j] and graph[i][j] != '#':
      bfs(i, j)

print(sheeps, wolves)