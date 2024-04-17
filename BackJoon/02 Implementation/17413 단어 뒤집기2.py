'''
17413 단어 뒤집기2

주어진대로 구현
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
answer = ""

word = ""
switch = False # <, > 안에 있는지 검사
for i in range(len(s)):
    # > 이면 switch 꺼주기
    if s[i] == ">":
        switch = False
    
    # <, > 안에 있으면 다 그대로 더해주기
    if switch:
        word += s[i]
    else:
        if s[i] == "<":
            switch = True
            answer += "".join(reversed(word))
            word = s[i]
        elif s[i] == ">":
            word += s[i]
            answer += word
            word = ""
        elif s[i] == " ":
            answer += "".join(reversed(word))
            answer += " "
            word = ""
        else:
            word += s[i]

if word:
    answer += "".join(reversed(word))

print(answer)