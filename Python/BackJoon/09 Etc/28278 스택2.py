'''
28278 스택2
재귀함수의 근간이 되는 스택문제
'''

import sys
input = sys.stdin.readline

stack = []

def stack_2():
    if stack:
        return stack.pop()
    else:
        return -1

def stack_4():
    if stack:
        return 0
    else:
        return 1

def stack_5():
    if stack:
        return stack[-1]
    else:
        return -1

for _ in range(int(input())):
    prompt = list(map(int, input().split()))
    if prompt[0] == 1:
        stack.append(prompt[1])
    elif prompt[0] == 2:
        print(stack_2())
    elif prompt[0] == 3:
        print(len(stack))
    elif prompt[0] == 4:
        print(stack_4())
    elif prompt[0] == 5:
        print(stack_5())
