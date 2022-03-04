# 2589번 보물섬

# 최단거리 문젠데,, 모두 중복없이 방문하는 것이므로 bfs/dfs를 쓰는 게 좋을거같아서 그렇게 품
# 원래 최단거리는 dp나 다익스트라 플로이드..!

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
  graph.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_search(x, y):
  q = deque([(x, y, 0)])
  visited = [[0] * m for _ in range(n)]
  distance = [[0] * m for _ in range(n)]
  visited[x][y] = 1
  distance[x][y] = 0
  ans = 0
  
  while q:
    a, b, cost = q.popleft()
    for i in range(4):
      rx = a + dx[i]
      ry = b + dy[i]
      if 0 <= rx < n and 0 <= ry < m and not visited[rx][ry] and graph[rx][ry] == 'L':
        distance[rx][ry] = cost+1
        visited[rx][ry] = 1
        q.append((rx, ry, distance[rx][ry]))
    ans = max(ans, cost)
  return ans

max_value = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      max_value = max(max_value, bfs_search(i, j))

print(max_value)