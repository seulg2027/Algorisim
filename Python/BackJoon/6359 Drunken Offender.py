# 6359번 만취한 상범

import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
  n = int(input())
  dp = [0] * (n+1)
  dp[1] = 1
  cnt = 0
  
  for i in range(2, n+1):
    for j in range(2, i+1):
      if i % j == 0:
        cnt += 1
    if cnt % 2 == 0:
      dp[i] = dp[i-1] + 1
    else:
      dp[i] = dp[i-1]
    cnt = 0
  
  result.append(dp[n])

for i in result:
  print(i)