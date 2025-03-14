# 1965번 상자넣기

# # 보류
# import sys
# input = sys.stdin.readline

# n = int(input())
# boxes = list(map(int, input().split()))
# dp = [0 for _ in range(n)]
# dp[0] = 1

# for i in range(1, n):
#   temp = boxes[0]
#   for j in range(i+1):
#     if temp < boxes[j] <= boxes[i]:
#       temp = boxes[j]
#       dp[i] += 1
#       if i == 4:
#         print('i=', i, 'j=', j, "temp=", temp)
#         print(dp[i])
#       max_value = max(dp[i-1], dp[i])
#   dp[i] = max_value

# print(dp)

# 답 봄... 하 정답에 근접은 한거로 일단 만족,, 언제 dp 실버문제 마스터할까ㅠㅠ

import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))
dp = [1 for _ in range(n+1)]

if n == 1:
  print(1)
else:
  for i in range(2, n+1):
    for j in range(1, i+1):
      if boxes[j-1] < boxes[i-1]:
        dp[i] = max(dp[j] + 1, dp[i])
  print(max(dp))