'''
15656번 N과 M(7)

기본 백트래킹
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))

seq.sort()

res = []

def backtracking(x):
    if x == M:
        print(*res)
        return
    
    for i in range(N):
        res.append(seq[i])
        backtracking(x+1)
        res.pop()

backtracking(0)
