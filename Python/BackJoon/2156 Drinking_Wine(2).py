# 2156번 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
w = [0] + [int(input()) for _ in range(n)] + [0]
dp = [0] * (n+2)
dp[1] = w[1]
dp[2] = w[1] + w[2]

for i in range(3, n+1):
  dp[i] = max(dp[i-2], w[i-1] + dp[i-3]) + w[i]
  for j in range(1, i):
    if dp[i] < dp[j]:
      dp[i] = dp[j]

print(dp[n])