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

# 피보나치 수 

N = int(input())

mod = 1000000
fibo = [0, 1]
p = mod // 10 * 15

for i in range(2,p):
  fibo.append(fibo[i-1]+fibo[i-2])
  fibo[i] %= mod

print(fibo[N%p])