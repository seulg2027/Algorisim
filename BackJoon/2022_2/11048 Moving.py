# 11048번 이동하기

# dp 문제 한번에 클리어해서 기쁘당

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [[0 for _ in range(m+1)]]
for _ in range(n):
  miro += [[0] + list(map(int, input().split()))]
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, m+1):
  for j in range(1, n+1):
    if i == 1:
      dp[j][i] = dp[j-1][i] + miro[j][i]
    elif j == 1:
      dp[j][i] = dp[j][i-1] + miro[j][i]
    else:
      dp[j][i] = max(dp[j-1][i], dp[j][i-1]) + miro[j][i]

print(dp[n][m])