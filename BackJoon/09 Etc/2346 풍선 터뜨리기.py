'''
2346번 풍선 터뜨리기
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
balloons = list(map(int, input().split()))
moving = deque(list((i+1, balloons[i]) for i in range(n))) #풍선 번호, 풍선 숫자 모두 저장
answer = []

for _ in range(n):
    now = moving.popleft()
    if now[1] > 0:
        moving.rotate(-(now[1]-1))
    else:
        moving.rotate(-now[1])
    answer.append(now[0])

for a in answer:
    print(a, end=" ")