# 11722번 가장 긴 감소하는 부분 수열

# dp

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
  for j in range(i+1):
    if seq[i] < seq[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp))