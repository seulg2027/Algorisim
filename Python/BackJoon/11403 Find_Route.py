# 11403번 경로 찾기

# n <= 100 이라는 제한이 있으므로 플로이드

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * (n+1)]

for _ in range(n):
  graph += [[0] + list(map(int, input().split()))]

for k in range(1, n+1):
  for j in range(1, n+1):
    for i in range(1, n+1):
      if graph[i][k] + graph[k][j] > 1:
        graph[i][j] = 1

for i in range(1, n+1):
  for j in range(1, n+1):
    print(graph[i][j], end=' ')
  print()