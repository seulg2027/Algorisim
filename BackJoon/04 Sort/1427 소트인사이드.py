"""
1427번 소트인사이드
"""

import sys

input = sys.stdin.readline

n = list(map(int, input().rstrip()))
n.sort(reverse=True)
print("".join(map(str, n)))
