'''
28279번 덱2
덱도 index사용 가능
'''

import sys
from collections import deque
input = sys.stdin.readline

q = deque([])

for _ in range(int(input())):
    command = list(input().split())
    
    if command[0] == "1":
        q.appendleft(command[1])
    elif command[0] == "2":
        q.append(command[1])
    elif command[0] == "3":
        print(q.popleft()) if q else print(-1)
    elif command[0] == "4":
        print(q.pop()) if q else print(-1)
    elif command[0] == "5":
        print(len(q))
    elif command[0] == "6":
        print(0) if q else print(1)
    elif command[0] == "7":
        print(q[0]) if q else print(-1)
    elif command[0] == "8":
        print(q[-1]) if q else print(-1)