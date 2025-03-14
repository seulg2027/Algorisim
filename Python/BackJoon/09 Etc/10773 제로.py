'''
10773 제로
'''

import sys
input = sys.stdin.readline

integers = []
for _ in range(int(input())):
    c = int(input())
    if c == 0:
        integers.pop()
    else:
        integers.append(c)

print(sum(integers)) if integers else print(0)
