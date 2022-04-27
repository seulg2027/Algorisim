# 2206번 벽 부수고 이동하기

## bfs 3차원 배열... queue 길이 줄여서 메모리 크기 맞추느라 고생했음

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
  q = deque([(0, 0, 0)])
  visited[0][0][0] = 1
  while q:
    x, y, z = q.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][z]
    for i in range(4):
      rx = x + dx[i]
      ry = y + dy[i]
      if rx < 0 or rx >= n or ry < 0 or ry >= m:
        continue
      if graph[rx][ry] == 0 and not visited[rx][ry][z]:
        visited[rx][ry][z] = visited[x][y][z] + 1
        q.append((rx, ry, z))
      elif graph[rx][ry] == 1 and z == 0:
        visited[rx][ry][1] = visited[x][y][0] + 1
        q.append((rx, ry, 1))
  return -1

print(bfs())