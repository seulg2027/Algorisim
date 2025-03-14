# 4963번 섬의 개수

# dfs 복습

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, visited):
  global w, h
  if 0 <= x < h and 0 <= y < w:
    if not visited[x][y] and maps[x][y] == 1:
      visited[x][y] = 1
      for i in range(8):
        rx = x + dx[i]
        ry = y + dy[i]
        dfs(rx, ry, visited)
      return True
  return False

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  maps = []
  for _ in range(h):
    maps += [list(map(int, input().split()))]
  visited = [[0] * w for _ in range(h)]
  
  cnt = 0
  for i in range(h):
    for j in range(w):
      if dfs(i, j, visited) == True:
        cnt += 1
  print(cnt)