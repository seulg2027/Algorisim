'''
2002번 추월
정렬을 이용하니까 바로 풀렸당
'''

import sys
input = sys.stdin.readline

n = int(input())
licenses = dict()
for i in range(n):
    licenses[input().rstrip()] = i # 차량에 순서 매기기

exit_list = []
for _ in range(n):
    exit_list.append(licenses[input().rstrip()]) # 출구에 나온 순서대로 리스트

answer = 0
for i in range(n):
    is_over = False
    for j in range(i, n):
        if exit_list[i] > exit_list[j]:
            is_over = True
    if is_over:
        answer += 1

print(answer)