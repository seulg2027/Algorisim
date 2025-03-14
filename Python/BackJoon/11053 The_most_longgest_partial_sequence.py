# 11053번 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, i):
    if a[j] < a[i]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))