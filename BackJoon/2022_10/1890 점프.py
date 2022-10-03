# 1890번 점프

# 처음엔 dfs인 줄 알았으나 경우의 수가 최대 2^64개라는 걸 보고 바로 접음
# 재귀함수를 쓰지 않는 dp로 결정

import sys
input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if i == n-1 and j == n-1:
      break
    if 0 <= i + game[i][j] < n:
      dp[i + game[i][j]][j] += dp[i][j]
    if 0 <= j + game[i][j] < n:
      dp[i][j + game[i][j]] += dp[i][j]
    dp[i][j] = 0

print(dp[n-1][n-1])