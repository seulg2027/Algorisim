# 9095번 1, 2, 3 더하기

import sys
input = sys.stdin.readline

results = []

for _ in range(int(input())):
  n = int(input())
  dp = [0 for _ in range(n+1)]
  if n < 4:
    dp = [0] * 5
  dp[1], dp[2], dp[3], dp[4] = 1, 2, 4, 7
  for i in range(5, n+1):
    dp[i] = 2 * dp[i-1] - dp[i-4]
  results.append(dp[n])

for ans in results:
  print(ans)