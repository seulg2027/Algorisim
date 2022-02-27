# 9465번 스티커

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  stickers = []
  dp = [[0] * n for _ in range(2)]
  for _ in range(2):
    stickers += [list(map(int, input().split()))]
  if n >= 2:
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    dp[0][1] = dp[1][0] + stickers[0][1]
    dp[1][1] = dp[0][0] + stickers[1][1]
    max_value = max(dp[0][1], dp[1][1])
    for i in range(2, n):
      for j in range(2):
        dp[j][i] = stickers[j][i] + max(dp[abs(j-1)][i-2], dp[abs(j-1)][i-1])
        max_value = max(max_value, dp[j][i])
    print(max_value)
  else:
    print(max(stickers[0][0], stickers[1][0]))
