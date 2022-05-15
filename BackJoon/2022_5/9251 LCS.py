# 9251번 LCS

# 동적 계획법 사용
# 너모 어렵다ㅠㅠ 동적계획법 한번 더 사용해서 풀어보자

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s1_list = [0] + list(s1)
s1_len = len(s1)
s2 = input().rstrip()
s2_list = [0] + list(s2)
s2_len = len(s2)
dp = [[0] * (s1_len+1) for _ in range(s2_len+1)]

for i in range(1, s1_len+1):
  for j in range(1, s2_len+1):
    if s1_list[i] == s2_list[j]:
      dp[j][i] = dp[j-1][i-1]+1
    else:
      dp[j][i] = max(dp[j][i-1], dp[j-1][i])

print(dp[-1][-1])