# 1058번 친구

import sys
input = sys.stdin.readline

# dfs로 시도.. 그런데 자꾸 틀림

# n = int(input())
# friends = []
# graph = [[] for _ in range(n+1)]

# for i in range(n):
#   people = list(input().strip())
#   for j in range(n):
#     if people[j] == 'Y':
#       graph[i+1].append(j+1)

# def dfs(v, level):
#   global value
#   if level < 2:
#     visited[v] = True
#     for i in graph[v]:
#       if not visited[i]:
#         value += 1
#         visited[i] = True
#         dfs(i, level + 1)

# ans = 0

# for i in range(1, n+1):
#   visited = [False for _ in range(n+1)]
#   value = 0
#   dfs(i, 0)
#   ans = max(value, ans)

# print(ans)

# 최대값을 구하는 것, 2친구를 구하는 개념 => 플로이드 와샬

n = int(input())

friend = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    for k in range(n):
      if j == k : continue
      
      if friend[j][k] == 'Y' or (friend[j][i] == 'Y' and friend[i][k] == 'Y'):
        visited[j][k] = 1

result = 0

for i in visited:
  result = max(result, sum(i))

print(result)