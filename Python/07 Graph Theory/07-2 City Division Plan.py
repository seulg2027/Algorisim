# 07-2 도시 분할 계획

# 내가 푼 방법
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

edges = []

for _ in range(M):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()
result = 0
last = 0

for edge in edges:
  cost, a, b = edge
  # 같은 집합에 포합되어 있지 않을 경우만 집합에 포함시킴
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a != b:
    # 각 노드의 루트노드를 갖는 노드가 전체 집합을 이루지 않을 경우만
    last = cost
    union_parent(parent, a, b)
    result += cost

print(result - last)