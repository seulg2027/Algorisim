'''
10819 차이를 최대로
'''

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
option = list(permutations(arr, N))
answer = 0

for o in option:
    res = 0
    for i in range(1, N):
        res += abs(o[i-1] - o[i])
    answer = answer if answer > res else res

print(answer)
