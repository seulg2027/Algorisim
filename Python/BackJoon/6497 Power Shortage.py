# 6497번 전력난

import sys
input = sys.stdin.readline

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

totals =[]

while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0:
    break
  parent = [i for i in range(m)]
  roads = []
  total = 0
  
  for i in range(n):
    a, b, t = map(int, input().split())
    roads.append((t, a, b))
    total += t
  
  roads.sort()
  
  for road in roads:
    t, a, b = road
    if find_parent(a) != find_parent(b):
      union_parent(a, b)
      total -= t
  totals.append(total)

for t in totals:
  print(t)