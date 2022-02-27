# 4386 별자리 만들기 크루스칼 복습
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# parent = [i for i in range(n+1)]
# visited = [False for _ in range(n+1)]
# edges = []
# for _ in range(m):
#   a, b, price = map(int, input().split())
#   edges.append((price, a, b))

# edges.sort()

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

# result = 0
# for edge in edges:
#   cost, a, b = edge
#   if find_parent(a) != find_parent(b):
#     union_parent(a, b)
#     result += cost

# print(result)