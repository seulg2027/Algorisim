'''
4949번 균형잡힌 세상
스택
'''

import sys
input = sys.stdin.readline

while True:
    string = input()
    stack = []
    is_yes = True
    if string[0] == '.' and len(string) == 2:
        break
    
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[":
            stack.append(string[i])
        elif string[i] == ")":
            if stack:
                item = stack.pop()
                if item != "(":
                    is_yes = False
            else: is_yes = False
        elif string[i] == "]":
            if stack:
                item = stack.pop()
                if item != "[":
                    is_yes = False
            else: is_yes = False
    if stack: is_yes = False
    
    print("yes" if is_yes else "no")