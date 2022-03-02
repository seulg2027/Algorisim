# 1389번 케빈 베이컨의 6단계 법칙

# bfs로 품 다익스트라 ㄴㄴ

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  if not b in graph[a]:
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
  distance = [sys.maxsize for _ in range(n+1)]
  visited = [False for _ in range(n+1)]
  distance[0], distance[start] = 0, 0
  q = deque([(start, 0)])
  visited[start] = True
  while q:
    now, dist = q.popleft()
    for i in graph[now]:
      if distance[i] > dist+1:
        distance[i] = dist+1
      if not visited[i]:
        q.append((i, dist+1))
        visited[i] = True
  return sum(distance)

result = []
for i in range(1, n+1):
  result.append(bfs(i))
ans = min(result)

print(result.index(ans) + 1)