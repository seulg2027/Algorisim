# 1944번 복제 로봇

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
graph = []
start = []
keys = []
temp_key = []
for i in range(n):
  graph += [list(map(str, input().rstrip()))]
  for j in range(n):
    parent[i][j] = (i, j)
    if graph[i][j] == 'S':
      start.append((i, j))
    if graph[i][j] == 'K':
      keys.append((i, j))
      temp_key.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = -1

def check():
  for key in temp_key:
    a, b = key
    if parent[a][b] != [start[0]]:
      return False
  return True

def dfs(x, y, cnt):
  global result
  if not keys:
    print(visited)
    result = cnt
    return
  visited[x][y] = True
  for i in range(4):
    rx = x + dx[i]
    ry = y + dy[i]
    if 0 <= rx < n and 0 <= ry < n and not visited[rx][ry]:
      if graph[rx][ry] == 'K' and parent[rx][ry] != start[0]:
        keys.remove((rx, ry))
        parent[rx][ry] = start
        visited[rx][ry] = True
        dfs(rx, ry, cnt+1)
        keys.append((rx, ry))
        parent[rx][ry] = (rx, ry)
        visited[rx][ry] = False
      if graph[rx][ry] == '0' and parent[rx][ry] != start[0]:
        parent[rx][ry] = start
        visited[rx][ry] = True
        dfs(rx, ry, cnt+1)
        parent[rx][ry] = (rx, ry)
        visited[rx][ry] = False

dfs(start[0][0], start[0][1], 0)
print(result)