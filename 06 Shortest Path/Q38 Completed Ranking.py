# Q38 정확한 순위

INF = int(1e9)

# 플로이드 워셜 알고리즘
N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

result = [1] * (N+1)
result[0] = 0

for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      graph[i][j] = 0

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = 1

for a in range(1, N+1):
  for b in range(1, N+1):
    for c in range(1, N+1):
      graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c]) #무한 숫자를 갱신

for i in range(1, N+1):
  for j in range(i, N+1):
    if graph[i][j] == INF and graph[j][i] == INF:
      result[i] = 0
      result[j] = 0

print(result.count(1))