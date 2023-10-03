'''
11866 요세푸스 문제 0
'''

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = [i for i in range(1, n+1)]
answer = []
circle_q = deque(numbers)

for j in range(1, n+1):
    circle_q.rotate(-(k-1))
    a = circle_q.popleft()
    answer.append(a)

for a in range(n):
    if a == 0:
        print("<", end="")
    if a == n-1:
        print(answer[a], end=">")
    else:
        print(answer[a], end=", ")