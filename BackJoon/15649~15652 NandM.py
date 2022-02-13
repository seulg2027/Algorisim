# 15649 ~ 15652 N과 M

# # 15649번 N과 M(1)
# # 기본 백트래킹

# n, m = map(int, input().split())

# visited = [0] * (n+1)
# arr = [0] * (m+1)

# def check(x):
#   global n, m
#   if x == m+1:
#     for i in range(1, m+1):
#       print(arr[i], end=' ')
#     print()
#   else:
#     for i in range(1, n+1):
#       if not visited[i]:
#         visited[i] = 1
#         arr[x] = i
#         check(x+1)
#         arr[x] = 0
#         visited[i] = 0

# check(1)

# # 15650번 N과 M(2)
# # nCm 구하기

# n, m = map(int, input().split())

# visited = [0] * (n+1)
# arr = [0] * (m+1)

# def dfs_combination(x):
#   global n, m
#   if x == m+1:
#     for i in range(1, m+1):
#       print(arr[i], end=' ')
#     print()
#   else:
#     for i in range(1, n+1):
#       if max(arr) < i:
#         arr[x] = i
#         dfs_combination(x+1)
#         arr[x] = 0

# dfs_combination(1)


# # 15651번 N과 M(3)
# # 순열 구하기

# n, m = map(int, input().split())

# arr = [0] * (m+1)

# def dfs_combination(x):
#   global n, m
#   if x == m+1:
#     for i in range(1, m+1):
#       print(arr[i], end=' ')
#     print()
#   else:
#     for i in range(1, n+1):
#       arr[x] = i
#       dfs_combination(x+1)
#       arr[x] = 0

# dfs_combination(1)


# 15652번 N과 M(4)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * (m+1)

def check(x):
  global n, m
  if x == m+1:
    for i in range(1, m+1):
      print(arr[i], end=' ')
    print()
  else:
    for i in range(1, n+1):
      if x > 1:
        arr[x] = i
        if arr[x-1] <= arr[x]:
          check(x+1)
        arr[x] = 0
      else:
        arr[x] = i
        check(x+1)
        arr[x] = 0

check(1)