# 06-2 전보

import heapq

INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)] # 그래프
dist = [INF] * (N+1) # 최단 거리 초기화

# 그래프 설정
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  # 거리, 노드번호
  heapq.heappush(q, (0, start))
  dist[start] = 0
  while q: # 큐가 빌 때까지
    distance, now = heapq.heappop(q)
    if dist[now] < distance:
      continue
    for i in graph[now]:
      if distance + i[1] < dist[i[0]]:
        dist[i[0]] = distance + i[1]
        heapq.heappush(q, (distance + i[1], i[0]))

dijkstra(C)

cnt = 0

for i in range(N+1):
  if dist[i] != INF:
    cnt += 1


print(cnt - 1, end=" ")
print(max(dist))