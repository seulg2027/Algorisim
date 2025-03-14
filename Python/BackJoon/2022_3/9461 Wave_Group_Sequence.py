# 9461번 파도반 수열

# dp 연습

import sys
input = sys.stdin.readline

dp = [0] * 101
dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

for _ in range(int(input())):
  n = int(input())
  if n > 5:
    for i in range(6, n+1):
      dp[i] = dp[i-5] + dp[i-1]
  print(dp[n])