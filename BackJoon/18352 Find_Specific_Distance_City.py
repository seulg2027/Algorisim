# 18352번 특정 거리의 도시 찾기

# 다익스트라

import heapq, sys

input = sys.stdin.readline
inf = sys.maxsize

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]

for _ in range(m):
  v, u = map(int, input().split())
  graph[v].append(u)

q = []
distance[x] = 0
heapq.heappush(q, (0, x))
while q:
  cost, now = heapq.heappop(q)
  for v in graph[now]:
    d = cost + 1
    if d < distance[v]:
      distance[v] = d
      heapq.heappush(q, (d, v))

if k in distance:
  for i in range(1, n+1):
    if distance[i] == k:
      print(i)
else:
  print(-1)