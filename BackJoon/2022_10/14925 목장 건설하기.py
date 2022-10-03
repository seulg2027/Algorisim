# 14925번 목장 건설하기

# 구현인건가?.?
# 알고보니 dp

# 시간초과

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
pasture = [list(map(int, input().split())) for _ in range(m)]
max_value = 1

# L = 원하는 직사각형의 길이
for L in range(min(m, n)):
  s = min(m, n) - L + 1
  for i in range(s):
    for j in range(s):
      is_value = True
      for k in range(L):
        if 1 in pasture[i+k][j:j+L] or 2 in pasture[i+k][j:j+L]:
          is_value = False
      if is_value:
        max_value = L

print(max_value)


# dp 정답 코드

m, n=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(m)]
dp=[[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
  if grid[i][0]==0:
    dp[i][0]=1

for j in range(n):
  if grid[0][j]==0:
    dp[0][j]=1

for i in range(1, m):
  for j in range(1, n):
    if grid[i][j]==0:
      dp[i][j]=min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
answer=0
for i in range(m):
  answer=max(answer, max(dp[i]))

print(answer)