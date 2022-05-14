# 9205번 맥주 마시면서 걸어가기

# dfs 풀이,, 시간초과 극심하게 났음
# bfs 로 변경해 풀이

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append([graph[1][0], graph[1][1]])
  while q:
    x, y = q.popleft()
    if abs(x-graph[n+2][0]) + abs(y-graph[n+2][1]) <= 1000:
      print("happy")
      return
    for i in range(2, n+2):
      if not visited[i]:
        nx, ny = graph[i]
        if abs(x-nx) + abs(y-ny) <= 1000:
          q.append([nx, ny])
          visited[i] = 1
  print("sad")
  return

for _ in range(int(input())):
  n = int(input())
  
  graph = [(0, 0)]
  for _ in range(n+2):
    x, y = map(int, input().split())
    graph.append((x, y))
  
  visited = [0 for _ in range(n+3)]
  visited[1] = 1
  bfs()


## dfs

# def dfs(v, visited):
#   global is_go
#   for i in range(2, n+3):
#     if not visited[i]: # 방문하지 않았을 경우에만 계산
#       diff = abs(graph[i][0] - graph[v][0]) + abs(graph[i][1] - graph[v][1])
#       if diff <= 1000:
#         visited[i] = 1
#         dfs(i, visited)
#         visited[i] = 0
#   if visited[n+2]:
#     is_go = True