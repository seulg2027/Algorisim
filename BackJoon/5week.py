# # 설탕 배달

# n = int(input())

# cnt = 0

# while n >= 0:
#   if n % 5 == 0:
#     cnt += n // 5
#     print(cnt)
#     break
#   n -= 3
#   cnt += 1
# else: 
#   print(-1)

# # RGB 거리

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# for i in range(1, n):
#   graph[i][0] = graph[i][0] + min(graph[i-1][1], graph[i-1][2])
#   graph[i][1] = graph[i][1] + min(graph[i-1][0], graph[i-1][2])
#   graph[i][2] = graph[i][2] + min(graph[i-1][0], graph[i-1][1])

# print(min(graph[n-1]))

# # 피보나치 수 3
# # 내가 푼 코드
# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [0] * 2
# dp[1] = 1

# def fibo():
#   for i in range(2, n+1):
#     dp[i % 2] = dp[0] + dp[1]
#   return dp[n % 2] % 1000000

# print(fibo())

# # 답지 코드

# N = int(input())

# mod = 1000000
# fibo = [0, 1]
# p = mod // 10 * 15

# for i in range(2,p):
#   fibo.append(fibo[i-1]+fibo[i-2])
#   fibo[i] %= mod

# print(fibo[N%p])

# 계단 오르기

import sys
input = sys.stdin.readline

# n = int(input())
# scores = [int(input()) for _ in range(n)]
# visited = [False for _ in range(n+1)]

# def max_score(idx):
#   if idx == n-2 or idx == n-3:
#     scores[n-1] += max(scores[n-2], scores[n-3])
#     return scores[n-1]
#   if scores[idx+1] > scores[idx+2]:
#     if idx >= 1 and visited[idx-1] == True:
#       visited[idx+2] = True
#       scores[idx+2] += scores[idx]
#       max_score(idx+2)
#     else:
#       visited[idx+1] = True
#       scores[idx+1] += scores[idx]
#       max_score(idx+1)
#   elif scores[idx+1] <= scores[idx+2]:
#     visited[idx+2] = True
#     scores[idx+2] += scores[idx]
#     max_score(idx+2)

# if n <= 2:
#   print(scores[0] + scores[1])
# else:
#   max_score(0)
#   print(scores[n-1])

# 답지
# n = int(input())
# scores = [0] + [int(input()) for _ in range(n)] + [0]
# cache = [0] * (n+2)
# cache[1] = scores[1]
# cache[2] = cache[1] + scores[2]

# for i in range(3, n+1):
#   cache[i] = max(cache[i-2], cache[i-3] + scores[i-1]) + scores[i]

# print(cache[n])