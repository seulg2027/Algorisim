# 미로 탐색

import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int,sys.stdin.readline().strip())) for i in range(n)]

def dfs(x, y, n, m, result):
  if x == n-1 and y == m-1:
    print(result)
    return result
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if maze[x][y] == 1:
    result += 1
    dfs(x-1, y, n, m, result)
    dfs(x, y-1, n, m, result)
    dfs(x+1, y, n, m, result)
    dfs(x, y+1, n, m, result)
    return result
  return False

dfs(0, 0, n, m, 0)