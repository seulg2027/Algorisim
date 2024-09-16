'''
플로이드 워셜 연습문제ㅎㅎ

i, j, k 위치 기억해야 함ㅠ
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
partys = list(list(map(int, input().split())) for _ in range(n))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            partys[i][j] = min(partys[i][j], partys[i][k] + partys[k][j])

for _ in range(m):
    a, b, c = map(int, input().split())
    if partys[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")
