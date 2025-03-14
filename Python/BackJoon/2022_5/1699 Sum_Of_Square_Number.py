# 1699번 제곱수의 합

# dp로 풀이

import sys, math
input = sys.stdin.readline

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, int(math.sqrt(n+1))+1):
  dp[i**2] = 1
  for j in range(i**2+1, n+1):
    dp[j] = min(dp[j], dp[i**2]+dp[j-i**2])

print(dp[-1])