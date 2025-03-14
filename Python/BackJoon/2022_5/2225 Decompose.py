# 2225번 합분해

# # 백트래킹으로 시도 -> 시간초과가 심각하게 남

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# arr = [0] * k
# visited = [0] * (n+1)
# cnt = 0

# def backtracking(x, idx):
#   global n, k, cnt
#   if x == k-1:
#     cnt += 1
#   else:
#     for i in range(idx+1):
#       arr[x] = i
#       backtracking(x+1, idx-i)
#       arr[x] = 0

# backtracking(0, n)
# print(cnt % 1000000000)

# DP인가.. 싶어서 다시 DP로 도전

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * (n+1) for _ in range(k)]

for i in range(1, k):
  for j in range(1, n+1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[k-1][n] % 1000000000)