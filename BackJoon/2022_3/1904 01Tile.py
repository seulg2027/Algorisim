# 1904번 01 타일

# 피보나치 수 였음

import sys
input = sys.stdin.readline

n = int(input())

dp = [1, 2]

for i in range(3, n+1):
  dp[i % 2 - 1] = (dp[0] + dp[1]) % 15746

print(dp[n % 2 - 1])