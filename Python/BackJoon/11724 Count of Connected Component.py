# 11724번 연결 요소의 개수

# # 서로소 집합 개념으로 풀이
# # 부모 값을 계속 갱신해줘야 하므로 사용 불가..

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# parent = [i for i in range(n+1)]

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

# for i in range(1, m+1):
#   a, b = map(int, input().split())
#   if find_parent(a) != find_parent(b):
#     union_parent(a, b)

# result = []
# for data in parent:
#   try:
#     vision = result.index(data)
#   except:
#     vision = -1
#   if data != 0 and vision == -1:
#     result.append(data)

# print(parent)


# DFS로 풀이
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(a):
  visited[a] = True
  for i in graph[a]:
    if not visited[i]:
      dfs(i)

cnt = 0
for i in range(1, n+1):
  if visited[i] == False:
    cnt += 1
    dfs(i)

print(cnt)