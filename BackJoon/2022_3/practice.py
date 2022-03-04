# # 코테 대비 문풀

# # # 2.
# from collections import deque
# import sys
# input = sys.stdin.readline

# p, n, h = map(int, input().split())
# pc = [h] * (p+1)
# check = [0] * (p+1)
# data = []
# for _ in range(n):
#   x, y = map(int, input().split())
#   check[x] = 1
#   if y <= h:
#     data.append((y, x))

# data.sort(reverse=True)
# q = deque(data)
# while q:
#   cost, a = q.popleft()
#   if pc[a] - cost >= 0:
#     pc[a] -= cost
#   else:
#     continue

# for i in range(p+1):
#   ans = (h - pc[i]) * 1000
#   if check[i]:
#     print(check[i], ans)

# # # 3. 슬라이딩 윈도우로 풀이

# import sys
# input = sys.stdin.readline

# n, m, e = map(int, input().split())
# beans = list(map(int, input().split()))
# beans.append(e)
# beans.sort()
# idx = beans.index(e)
# end = idx
# min_value = sys.maxsize

# for start in range(idx - m, idx+1):
#   sum_beans = beans[end] - beans[start]
#   end += 1
#   min_value = min(sum_beans, min_value)

# print(min_value)

# # # 4. 
# # 판을 벗어나는 것은 고려하지 않음

# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# data = list(map(int, input().split()))

# def bfs(start):
#   q = deque([(start, data[start])])
#   visited = [0 for _ in range(n)]
#   visited[start] = 1
#   while q:
#     now, cost = q.popleft()
#     if not visited[now + cost]:
#       q.append((now + cost, data[now + cost]))
#       visited[now + cost] = 1
#   return sum(visited)

# ans = 0
# for i in range(3):
#   ans = max(ans, bfs(i))

# print(ans+1)

# # 6. 토지 개발

# # # 이분 탐색 이용

# import sys
# input = sys.stdin.readline

# n = int(input())
# lands = list(map(int, input().split()))

# temp = n
# cnt = 0
# while temp > 1:
#   temp = temp // 2
#   cnt += 1

# def max_profit():
#   global cnt
#   result = 0
#   left = 0
#   right = n-1
#   count = 0
#   while cnt > count:
#     mid = (left + right) // 2
#     left_value = max(lands[left:mid+1])
#     right_value = max(lands[mid+1:right+1])
#     if left_value > right_value:
#       result += left_value
#       left = mid + 1
#     else:
#       result += right_value
#       right = mid
#     count += 1
#   return result

# print(max_profit())


# # 5. 두더지 게임

# # dp 기반으로 풀려고 노력

# import sys
# input = sys.stdin.readline

# n = int(input())
# game = []
# max_time = 0
# for i in range(n*n):
#   game += [list(map(int, input().split()))]
#   time = max(game[i][2:])
#   max_time = max(time, max_time)

# game = sorted(game, key=lambda x: x[0], reverse=True)
# scores = [0] * (max_time+1)
# scores[0] = -1
# cnt = 0

# while 0 in scores and cnt != len(game):
#   for i in range(game[cnt][1]):
#     scores[game[cnt][2+i]] = max(scores[game[cnt][2+i]], game[cnt][0])
#   cnt += 1

# print(sum(scores[1:]))


##### 코테 대비 기본 연습 #####

# # 1. 백트래킹 연습

# n, m = map(int, input().split())
# visited = [0] * (n+1)
# data = [i for i in range(1, n+1)]
# arr = [0] * (m+1)

# def backtracking(x):
#   if x == m+1:
#     for i in range(1, m+1):
#       print(arr[i], end=' ')
#     print()
#   else:
#     for i in range(n):
#       if not visited[i]:
#         visited[i] = 1
#         arr[x] = data[i]
#         backtracking(x+1)
#         arr[x] = 0
#         visited[i] = 0

# backtracking(1)

# # 조합

# n, m = map(int, input().split())
# visited = [0] * (n+1)
# data = [i for i in range(1, n+1)]
# arr = ''

# def backtracking(x):
#   global arr
#   if x == m+1:
#     for i in range(m):
#       print(arr[i], end=' ')
#     print()
#   else:
#     for i in range(n):
#       if not visited[i]:
#         idx = -1
#         if arr:
#           end = arr[-1]
#           idx = data.index(int(end))
#         if idx < i:
#           visited[i] = 1
#           arr += str(data[i])
#           backtracking(x+1)
#           arr = arr[:-1]
#           visited[i] = 0

# backtracking(1)


# # 2. 다익스트라 알고리즘

# import heapq

# n = int(input())
# distance = [int(1e9) for _ in range(n)]
# graph = [[] for _ in range(n+1)]

# for _ in range(n):
#   a, b, c = map(int, input().split())
# 	# a번 노드에서 b번 노드로 갈 경우 비용은 c
#   graph[a].append((b,c))

# def dijkstra(start):
#   q = []
#   heapq.heappush(q, (start, 0))
#   distance[start] = 0
#   while q:
#     now, dist = heapq.heappop(q)
#     if distance[now] < dist:
#       continue
#     for b, c in graph[now]:
#       cost = dist + c
#       if cost < distance[b]:
#         distance[b] = cost
#         heapq.heappush(q, (b, cost))

