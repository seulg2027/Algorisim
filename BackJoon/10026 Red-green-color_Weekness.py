# 10026번 적록색약

import sys, copy
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())
colors = []
for _ in range(n):
  colors += [list(input().rstrip())]

colors_week = copy.deepcopy(colors)
visited_week = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y, color):
  if 0 <= x < n and 0 <= y < n:
    if not visited[x][y] and colors[x][y] == color:
      visited[x][y] = 1
      dfs(x-1, y, color)
      dfs(x, y-1, color)
      dfs(x+1, y, color)
      dfs(x, y+1, color)
      return True
  return False

def dfs_week(x, y, color):
  if 0 <= x < n and 0 <= y < n:
    if color == "G":
      color = "R"
    if colors_week[x][y] == "G":
      colors_week[x][y] = "R"
    if not visited_week[x][y] and colors_week[x][y] == color:
      visited_week[x][y] = 1
      dfs_week(x-1, y, color)
      dfs_week(x, y-1, color)
      dfs_week(x+1, y, color)
      dfs_week(x, y+1, color)
      return True
  return False

cnt = 0
cnt_week = 0
for i in range(n):
  for j in range(n):
    if dfs(i, j, colors[i][j]) == True:
      cnt += 1
    if dfs_week(i, j, colors[i][j]) == True:
      cnt_week += 1

print(cnt, cnt_week)