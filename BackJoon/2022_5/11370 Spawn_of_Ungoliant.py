# 11370번 Spawn of Ungoliant

# 보자마자 dfs, bfs 생각남
# 그래프 특정 문자 바꾸기에는 bfs가 나을것 같아서 bfs 선택
# 반례없이 성공해서 기분조아>__<

from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  
  graph = []
  spiders = deque([])
  visited = [[0] * w for _ in range(h)]
  for i in range(h):
    graph.append(list(input().rstrip()))
    for j in range(w):
      if graph[i][j] == "S":
        spiders.append((i, j))
  
  while spiders:
    a, b = spiders.popleft()
    visited[a][b] = 1
    for i in range(4):
      rx = a + dx[i]
      ry = b + dy[i]
      if 0 <= rx < h and 0 <= ry < w:
        if graph[rx][ry] == "T" and not visited[rx][ry]:
          spiders.append((rx, ry))
          graph[rx][ry] = "S"
        visited[rx][ry] = 1
  
  for i in range(h):
    for j in range(w):
      print(graph[i][j], end='')
    print()