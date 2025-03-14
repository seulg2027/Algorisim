'''
1234
[3 : [1, 2], 1 : [2], 2 : []]
[4 : [1, 2], 3 : [2, 4], 1 : [3], 2 : [1]]
  1    2    3
[[2], [], [1, 2]] # 이긴 사람 적어두기
'''

import sys
input = sys.stdin.readline

n = int(input())
players = list(list(map(int, input().split())) for _ in range(n))
winner = dict()

for i in range(n):
    winner[i] = 0

for i in range(n):
    for j in range(i+1, n):
        strengthA = players[i][0] + players[j][0] * players[i][1]
        strengthB = players[j][0] + players[i][0] * players[j][1]
        if strengthA < strengthB:
            winner[j] += 1
        else:
            winner[i] += 1

result = sorted(winner.items(), key=lambda x: -x[1])

for res in result:
    print(res[0]+1)