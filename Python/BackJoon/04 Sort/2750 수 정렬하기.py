"""
2750번 수 정렬하기
"""

import sys

input = sys.stdin.readline

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
numbers.sort()
for n in numbers:
    print(n)
