# 2293번 동전1

# dp
# 원리 이해하기

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for j in range(k+1):
        if j - coin >= 0:
            dp[j] += dp[j-coin]

print(dp[k])