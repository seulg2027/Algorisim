'''
18258번 큐2
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
    command = list(input().split())
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "front":
        print(q[0]) if q else print(-1)
    elif command[0] == "back":
        print(q[-1]) if q else print(-1)
    elif command[0] == "pop":
        print(q[0]) if q else print(-1)
        if q:
            q.popleft()
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(0) if q else print(1)
