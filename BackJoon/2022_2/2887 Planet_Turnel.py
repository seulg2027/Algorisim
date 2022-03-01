# 2887번 행성 터널

# 크루스칼 트리 복습
# n이 크기 때문에 시간을 고려해서 풀어야함

import sys
input = sys.stdin.readline

n = int(input())
graph = []
parent = [i for i in range(n)]
for i in range(n):
  graph += [list(map(int, input().split())) + [i]]

def find_parent(x):
  if parent[x] != x:
    parent[x] = find_parent(parent[x])
  return parent[x]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

edges = []

#### 주의할 부분 ####
for i in range(3):
  graph.sort(key=lambda x:x[i])
  for j in range(1, n):
    edges.append((abs(graph[j-1][i] - graph[j][i]), graph[j-1][3], graph[j][3]))

edges.sort()
result = 0
cnt = 0
for edge in edges:
  price, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    result += price
    cnt += 1
  if cnt == n-1:
    break

print(result)