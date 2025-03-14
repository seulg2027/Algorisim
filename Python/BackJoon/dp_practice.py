# # 2579번 계단 오르기

# import sys
# input = sys.stdin.readline

# n = int(input())
# level = [0]
# level += [int(input()) for _ in range(n)]
# level += [0]
# dp = [0 for _ in range(n+2)]

# dp[1] = level[1]
# dp[2] = level[1] + level[2]

# for i in range(3, n+1):
#   dp[i] = level[i] + max(dp[i-2], dp[i-3]+level[i-1])

# print(dp[n])