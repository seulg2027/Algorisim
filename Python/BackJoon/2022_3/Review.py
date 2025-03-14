# 2644번 촌수계산

# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [0 for _ in range(n+1)]
# for _ in range(m):
#   x, y = map(int, input().split())
#   graph[x].append(y)
#   graph[y].append(x)

# def bfs(start, end):
#   q = deque([(0, start)])
#   visited[start] = 1
#   while q:
#     cost, now = q.popleft()
#     if now == end:
#       return cost
#     for i in graph[now]:
#       if not visited[i]:
#         visited[i] = 1
#         q.append((cost+1, i))
#   return None

# ans = bfs(a, b)
# if ans == None:
#   print(-1)
# else:
#   print(ans)


# # 1182번 부분수열의 합

# from itertools import combinations
# n, s = map(int, input().split())
# data = list(map(int, input().split()))

# cnt = 0

# for i in range(1, n+1):
#   integers = list(combinations(data, i))
#   for item in integers:
#     if sum(item) == s:
#       cnt += 1

# print(cnt)


