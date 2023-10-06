"""
25305번 커트라인
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
students = list(map(int, input().split()))

students.sort()
print(students[-k])
