# 11057번 오르막 수

# 10844번 풀이 생각하면 바로풀림

import sys, copy
input = sys.stdin.readline

n = int(input())
dp = [1] * 10
tmp = [1] * 10

if n >= 2:
  for i in range(1, n):
    for j in range(10):
      for m in range(0, j):
        dp[j] += tmp[m]
    d = copy.deepcopy(dp)
    tmp = d

print(sum(dp) % 10007)