'''
11047번 동전 0
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input().rstrip()) for _ in range(N))
coins.sort(reverse=True)
ans = 0

for coin in coins:
    ans += K // coin
    K = K % coin

print(ans)