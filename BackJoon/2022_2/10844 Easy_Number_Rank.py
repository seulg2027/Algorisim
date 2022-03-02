# 10844번 쉬운 계단 수

# dp 문제
# copy 가 한 몫 했던 문제,,,

import sys, copy
input = sys.stdin.readline

n = int(input())

dp = [1] * 10
temp = [1] * 10
dp[0], temp[0] = 0, 0

for i in range(2, n+1):
  for j in range(10):
    if j == 0:
      dp[j] = temp[j+1]
    elif j == 9:
      dp[j] = temp[j-1]
    else:
      dp[j] = temp[j-1] + temp[j+1]
  d = copy.deepcopy(dp)
  temp = d

print(sum(dp) % 1000000000)