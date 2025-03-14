# 촌수 계산

from collections import deque

n = int(input())
goal_l, goal_r = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
flag = False

for i in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

def dfs(s, result):
  global flag
  visited[s] = True
  for now in graph[s]:
    if not visited[now]:
      result += 1
      dfs(now, result)
      if now == goal_r:
        flag = True
        print(result)
      result -= 1

dfs(goal_l, 0)
if not flag:
  print(-1)