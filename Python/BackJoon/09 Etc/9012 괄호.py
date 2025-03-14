'''
9012 괄호
'''

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    tester = []
    string = input()
    is_VPS = True
    for i in range(len(string)):
        if string[i] == "(":
            tester.append(string[i])
        elif string[i] == ")":
            if tester:
                tester.pop()
            else:
                is_VPS = False
                break
    print("NO") if tester or is_VPS == False else print("YES")
