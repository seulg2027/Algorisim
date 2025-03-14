# 1922번 네트워크 연결

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
  a, b, price = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  edges.append((price, a, b))

edges.sort()

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

result = 0
for edge in edges:
  price, a, b = edge
  if find_parent(a) != find_parent(b):
    union_parent(a, b)
    result += price

print(result)