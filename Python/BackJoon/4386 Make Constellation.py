# 4386 별자리 만들기

import sys, math
input = sys.stdin.readline

n = int(input())
parent = [0] * (n+1)
graph = []

for i in range(1, n+1):
  x, y = map(float, input().split())
  parent[i] = i
  graph.append((x, y))

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

for i in range(n):
  for j in range(i, n):
    if i == j: continue
    cost = math.sqrt((graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2)
    edges.append((cost, i, j))

edges.sort()
result = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    result += cost

print(result)