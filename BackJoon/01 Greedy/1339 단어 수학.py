'''

순차적으로 9 ~ 0 부여
00GCF
ACDEB
{ A : 1, C : 2, D : 3, G : 4, E : 5, B : 6, F : 7 }
  5      4 3 2 1

가중치 부여하는 방식으로 풀기
'''

import sys
input = sys.stdin.readline

n = int(input())
words = list(input().rstrip() for _ in range(n))
alpha_code = dict()

# 가중치를 부여하기, 가중치는 10^(자릿수)
for i in range(n):
    for j in range(len(words[i])):
        if words[i][j] in alpha_code:
            alpha_code[words[i][j]] += 10 ** (len(words[i]) - j - 1)
        else:
            alpha_code[words[i][j]] = 10 ** (len(words[i]) - j - 1)

code_list = sorted(alpha_code.items(), key=lambda x: x[1], reverse=True)

number = 9
for code in code_list:
    alpha_code[code[0]] = number
    number -= 1

words_code = [''] * n

for i in range(n):
    for j in range(len(words[i])):
        words_code[i] += str(alpha_code[words[i][j]])

print(sum(int(i) for i in words_code))
