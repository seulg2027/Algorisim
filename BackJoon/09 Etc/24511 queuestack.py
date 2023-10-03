'''
24511번 queuestack
pop을 사용하는 모든 리스트를 deque로 해야 시간 초과가 안남
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))
m = int(input())
c_seq = deque(list(map(int, input().split())))

stack = deque([])

for i in range(n):
    if a_seq[i] == 0:
        stack.append(b_seq[i])

for j in range(m):
    if stack: # 미리 값이 있을 경우
        print(stack.pop(), end=' ')
    else:
        print(c_seq.popleft(), end=' ')

