# 1504번 특정한 최단 경로

import sys, heapq
input = sys.stdin.readline

inf = sys.maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, price = map(int, input().split())
  graph[a].append((b, price))
  graph[b].append((a, price))

v1, v2 = map(int, input().split())

def dijkstra(start):
  distance = [inf for _ in range(n+1)]
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for t, price in graph[now]:
      cost = dist + price
      if distance[t] > cost:
        distance[t] = cost
        heapq.heappush(q, (cost, t))
  return distance

dist_start = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)
cnt_1 = dist_start[v1] + dist_v1[v2] + dist_v2[n]
cnt_2 = dist_start[v2] + dist_v2[v1] + dist_v1[n]

if cnt_1 >= inf and cnt_2 >= inf:
  print(-1)
else:
  print(min(cnt_1, cnt_2))