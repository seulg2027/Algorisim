# 11660번 구간 합 구하기5

# 구간 합.. 무조건 첫 열, 첫 행은 0으로 초기화해주기!!

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1)]

for _ in range(n):
  graph.append([0] + list(map(int, input().split())))

# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

# 1 3 6 10
# 2 5 9 14
# 3 7 12 18
# 4 9 15 22

# 1 3 6 10
# 3 8 15 24
# 6 15 21 42
# 10 24 36 64

for i in range(1, n+1):
  for j in range(1, n):
    graph[i][j+1] += graph[i][j]

for i in range(1, n):
  for j in range(1, n+1):
    graph[i+1][j] += graph[i][j]

ans = []

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  ans.append(graph[x2][y2] - (graph[x2][y1-1] + graph[x1-1][y2] - graph[x1-1][y1-1]))

for a in ans:
  print(a)