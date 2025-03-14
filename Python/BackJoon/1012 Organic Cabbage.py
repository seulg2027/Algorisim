# 유기농 배추

import sys
sys.setrecursionlimit(100000)

def dfs(x, y, m, n, graph):
  if x <= -1 or x >= m or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y, m, n, graph)
    dfs(x, y-1, m, n, graph)
    dfs(x+1, y, m, n, graph)
    dfs(x, y+1, m, n, graph)
    return True
  return False

for _ in range(int(input())):
  m, n, k = map(int, input().split())
  graph = [[0] * n for _ in range(m)]
  for _ in range(k):
    l, r = map(int, input().split())
    graph[l][r] = 1
  result = 0
  for i in range(n):
    for j in range(m):
      if dfs(j, i, m, n, graph) == True:
        result += 1
  print(result)