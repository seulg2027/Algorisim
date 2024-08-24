'''
1455번 뒤집기2
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = [list(map(int, input().rstrip())) for _ in range(n)]
res = list([0] * m for _ in range(n))

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        # 먼저 이전 뒤집은 개수 가져오기
        if i == n-1 and j < m-1:
            res[i][j] = res[i][j+1]
        elif j == m-1 and i < n-1:
            res[i][j] = res[i+1][j]
        elif i < n-1 and j < m-1:
            res[i][j] = (res[i+1][j] - res[i+1][j+1]) + res[i+1][j+1] + (res[i][j+1] - res[i+1][j+1])
        
        # 뒤집어야 함
        if (coins[i][j] == 1 and res[i][j] % 2 == 0) or (coins[i][j] == 0 and res[i][j] % 2 != 0):
            res[i][j] += 1

print(res[0][0])