# 10451번 순열 사이클

import sys
input = sys.stdin.readline

sys.setrecursionlimit(2000)

def dfs(s, e):
  global cnt
  if s == e:
    cnt += 1
  else:
    if not visited[e]:
      visited[e] = 1
      dfs(s, data[e])

for _ in range(int(input())):
  n = int(input())
  data = [0] + list(map(int, input().split()))
  visited = [0 for _ in range(n+1)]
  
  cnt = 0
  for i in range(1, n+1):
    if not visited[i]: # 이부분을 처음에 빠뜨려서 틀림 # dfs에서 방문여부 꼭 확인..
      dfs(i, data[i])
  print(cnt)