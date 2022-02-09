# # 1932 정수 삼각형

# import sys
# input = sys.stdin.readline

# n = int(input())
# triangle = []
# for _ in range(n):
#   triangle += [list(map(int, input().split()))]

# for i in range(1, n):
#   for j in range(i + 1):
#     if j == 0:
#       triangle[i][j] += triangle[i-1][0]
#     elif j == i:
#       triangle[i][j] += triangle[i-1][j-1]
#     else:
#       triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# print(max(triangle[n-1]))

# # 1238 파티

# # 플로이드 워셜 코드 - 시간초과,,

# import sys
# input = sys.stdin.readline

# n, m, x = map(int, input().split())
# graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

# for i in range(m):
#   start, end, time = map(int, input().split())
#   graph[start][end] = time

# for k in range(1, n+1):
#   for i in range(1, n+1):
#     for j in range(1, n+1):
#       graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# def round_time(num):
#   global x
#   if num == x:
#     return 0
#   return graph[x][num] + graph[num][x]

# max_value = 0
# for idx in range(1, n+1):
#   max_value = max(max_value, round_time(idx))
# print(max_value)

# # 다익스트라로 다시 푼 코드
# import heapq
# import sys
# input = sys.stdin.readline

# n, m, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# result = [] * (n+1)

# for _ in range(m):
#   start, end, time = map(int, input().split())
#   graph[start].append((end, time))

# def to_go_dijkstra(start):
#   global x
#   q = []
#   distance = [int(1e9)] * (n+1)
#   heapq.heappush(q, (0, start))
#   distance[start] = 0
#   while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for i in graph[now]:
#       cost = dist + i[1]
#       if cost < distance[i[0]]:
#         distance[i[0]] = cost
#         heapq.heappush(q, (cost, i[0]))
#   return distance

# data = [0] * (n+1)
# for i in range(1, n+1):
#   if x == i:
#     result = to_go_dijkstra(i)
#   else:
#     data[i] = to_go_dijkstra(i)[x]

# for j in range(1, n+1):
#   result[j] += data[j]

# print(max(result[1:]))

# # 1753 최단 경로

# import heapq
# import sys
# input = sys.stdin.readline

# v, e = map(int, input().split())
# k = int(input())
# graph = [[] for _ in range(v+1)]
# distance = [int(1e9)] * (v+1)

# for _ in range(e):
#   start, end, weight = map(int, input().split())
#   graph[start].append((end, weight))

# def dijkstra(k):
#   q = []
#   heapq.heappush(q, (0, k))
#   distance[k] = 0
#   while q:
#     dist, now = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for item in graph[now]:
#       cost = dist + item[1]
#       if cost < distance[item[0]]:
#         distance[item[0]] = cost
#         heapq.heappush(q, (cost, item[0]))

# dijkstra(k)

# for data in distance[1:]:
#   if data == int(1e9):
#     print("INF")
#   else:
#     print(data)

# 17396 백도어

import sys
import heapq
inf=sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
alarm = list(map(int, input().split()))
alarm[-1] = 0
graph = [[] for _ in range(n)]
distance = [inf for _ in range(n)]

for _ in range(m):
  a, b, time = map(int, input().split())
  graph[a].append((b, time))
  graph[b].append((a, time))

q = []
heapq.heappush(q, (0, 0))
distance[0] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]] and alarm[i[0]] == 0:
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

print(distance[n-1]) if distance[n-1] < inf else print(-1)