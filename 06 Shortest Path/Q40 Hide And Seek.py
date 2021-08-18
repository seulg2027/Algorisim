# Q40 숨바꼭질

# 처음엔 다익스트라로 풀다가 플로이드로 돌림
# 왜냐하면 플로이드가 양방향이라서 더 구하기가 편하다고 판단했기 때문이다
# 플로이드로 답 구하고 다시 다익스트라로 품
INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
graph[1][0] = 0

for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      graph[i][j] = 0

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for a in range(1, N+1):
  for b in range(1, N+1):
    for c in range(1, N+1):
      graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

max_value = max(graph[1])
max_index = graph[1].index(max_value)
cnt = graph[1].count(max_value)

print(max_index, max_value, cnt)

# 다익스트라로 푼 풀이
import heapq
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

distance = [INF] * (N+1)
distance[0], distance[1] = 0, 0

def dijkstra():
  q = []
  heapq.heappush(q, (0, 1)) # 거리, 노드
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      if distance[i] > dist + 1:
        distance[i] = dist + 1
        heapq.heappush(q, (distance[i], i))

dijkstra()

print(distance.index(max(distance)), max(distance), distance.count(max(distance)))