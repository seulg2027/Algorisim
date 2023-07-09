'''
15654 N과 M(5)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

s = []

def backtracking(start):
    if len(s) == M:
        if len(set(s)) == M: # 리스트 내의 중복된 값이 없을 경우만 출력
            print(' '.join(map(str, s)))
            return
        return
    
    for i in range(N):
        s.append(n_list[i])
        backtracking(start+1)
        s.pop()

backtracking(1)
