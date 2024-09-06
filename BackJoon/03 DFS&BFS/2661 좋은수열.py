'''
1. 1, 2, 3을 활용해서 BackTracking을 활용해 수열을 만든다.
2. 수열을 만드는 과정에서, 좋은 수열인지 확인한다. -> 좋은 수열이면 계속 만듦 / 아니면 멈춤
3. 처음 만든 수열이 좋은 수열 중 가장 작은 수!
'''

import sys
input = sys.stdin.readline

n = int(input())
seq = ['0'] * n

def backtracking(x):
    if x == n:
        print("".join(seq)) # 바로 종료함
        sys.exit(0)
    
    for i in range(1, 4):
        seq[x] = str(i)
        if is_good_seq(seq, x+1):
            backtracking(x+1)
        seq[x] = '0'

def is_good_seq(s, x):
    for i in range(1, x // 2 + 1):
        if s[x-(i*2):x-i] == s[x-i:x]:
            return False
    return True

backtracking(0)