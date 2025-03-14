# Q37 플로이드

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
dist = [[INF] *(n+1) for _ in range(n+1)]

# 자기자신 거리 설정
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      dist[i][j] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  if dist[a][b] > c:
    dist[a][b] = c

for a in range(1, n+1):
  for b in range(1, n+1):
    for c in range(1, n+1):
      dist[b][c] = min(dist[b][c], dist[b][a] + dist[a][c])

for i in range(1, n+1):
  for j in range(1, n+1):
    if dist[i][j] != INF:
      print(dist[i][j], end=" ")
    else: # 만약 못 갈경우
      print(0, end=" ")
  print()