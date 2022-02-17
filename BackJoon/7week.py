# # 9372번 상근이의 여행

# import sys
# input = sys.stdin.readline

# def dfs(v, cnt):
#   visited[v] = 1
#   for i in graph[v]:
#     if visited[i] == 0:
#       cnt = dfs(i, cnt+1)
#   return cnt

# for _ in range(int(input())):
#   n, m = map(int, input().split())
#   graph = [[] for _ in range(n+1)]
#   visited = [0 for _ in range(n+1)]
  
#   for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
  
#   print(dfs(1, 0))

# # 1717번 집합의 표현

# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(10**9)

# n, m = map(int, input().split())

# def find_parent(x):
#   if parent[x] != x:
#     parent[x] = find_parent(parent[x])
#   return parent[x]

# def union_parent(a, b):
#   a = find_parent(a)
#   b = find_parent(b)
#   if a < b:
#     parent[b] = a
#   else:
#     parent[a] = b

# parent = {}

# for i in range(n+1):
#   parent[i] = i

# for _ in range(m):
#   is_union, a, b = map(int, input().split())
#   if is_union == 1:
#     if find_parent(a) == find_parent(b): print("YES")
#     else : print("NO")
#   else:
#     union_parent(a, b)

# 14567번 선수과목

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pre_graph = [[] for _ in range(n+1)]
subject = [0] + [1 for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  pre_graph[b].append(a)

for i in range(1, n+1):
  for sub in pre_graph[i]:
    subject[i] = max(subject[i], subject[sub]+1)

for j in range(1, n+1):
  print(subject[j], end=' ')