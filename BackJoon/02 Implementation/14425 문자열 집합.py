"""
14425번 문자열 집합
* 집합 포함 여부를 묻는 문제
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
answer = 0

for _ in range(n):
    a = input()
    s.add(a)

for _ in range(m):
    b = input()
    if b in s:
        answer += 1

print(answer)
