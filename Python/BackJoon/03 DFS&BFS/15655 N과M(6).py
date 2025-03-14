'''
15655번 N과 M(6)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort() # 정렬

s = [0] # max(s) 에서 오류가 나지 않게 방지

def backTracking(start):
    if len(s) == M+1:
        print(' '.join(map(str, s[1:])))
        return
    
    for i in range(N):
        if max(s) < n_list[i]: # 뒷자리 수가 앞자리 수보다 커야 함
            s.append(n_list[i])
            backTracking(start+1)
            s.pop()

backTracking(1)
