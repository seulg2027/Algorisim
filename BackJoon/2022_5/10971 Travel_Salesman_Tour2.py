# 10971번 외판원 순회2

# 백트래킹 도전

import sys
input = sys.stdin.readline

n = int(input())
parent = [i for i in range(n+1)]
graph = []

for i in range(n):
  cities = list(map(int, input().split()))
  l = []
  for j in range(n):
    if cities[j] == 0 and i != j:
      l.append(sys.maxsize)
    else:
      l.append(cities[j])
  graph.append(l)

visited = [0] * n
arr = [0] * n
result = sys.maxsize

def backtracking(x):
  global result, n
  if x == n:
    ans = 0
    for i in range(n-1):
      ans += graph[arr[i]][arr[i+1]]
    ans += graph[arr[-1]][arr[0]]
    result = min(ans, result)
  else:
    for j in range(1, n):
      if not visited[j]:
        visited[j] = 1
        arr[x] = j
        backtracking(x+1)
        arr[x] = 0
        visited[j] = 0

backtracking(1)

print(result)