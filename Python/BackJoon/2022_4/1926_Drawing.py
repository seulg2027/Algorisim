# 1926번 그림

# dfs

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
drawing = []
for _ in range(n):
  drawing.append(list(map(int, input().split())))

def dfs(x, y):
  global value
  if 0 <= x < n and 0 <= y < m:
    if drawing[x][y] == 1:
      value += 1
      drawing[x][y] = 0
      dfs(x+1, y)
      dfs(x, y+1)
      dfs(x-1, y)
      dfs(x, y-1)
      return True
  return False

ans = []
cnt = 0
for i in range(n):
  for j in range(m):
    value = 0
    if dfs(i, j) == True:
      cnt += 1
      ans.append(value)

print(cnt)
print(max(ans)) if ans else print(0)
