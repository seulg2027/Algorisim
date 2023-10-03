'''
2292 벌집
최대한 덜 반복문을 돌게 하는 방법?
'''

import sys
input = sys.stdin.readline

N = int(input())
honeycomb = 1
cnt = 0

while True:
    honeycomb += 6 * cnt
    if N <= honeycomb:
        break
    cnt += 1

print(cnt+1)