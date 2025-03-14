"""
10989번 수 정렬하기3
"""

import sys

input = sys.stdin.readline

numbers = [0] * 10001

for _ in range(int(input())):
    numbers[int(input())] += 1

for i in range(10001):
    if numbers[i] > 0:
        for j in range(numbers[i]):
            print(i)
