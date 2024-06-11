'''
15486번 퇴사2
'''

import sys
input = sys.stdin.readline

N = int(input())
t, p = [0 for _ in range(N+1)], [0 for _ in range(N+1)]

for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1]) # 이전까지의 최댓값
    if t[i] + i - 1 <= N:
        # 원래 dp값 / dp[i-1] + 새로운 값
        dp[t[i] + i-1] = max(dp[t[i] + i-1], p[i] + dp[i-1])

print(max(dp))