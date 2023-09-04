'''
1120 문자열
좀 더 쉽게 풀 수 있는 방법이 무조건 있을 것..
'''

import sys
input = sys.stdin.readline

A, B = input().split()
minus = abs(len(A) - len(B))
max_value = A if len(A) - len(B) > 0 else B
min_value = A if len(A) - len(B) <= 0 else B
min_len = len(A) if len(A) - len(B) <= 0 else len(B)

ans = sys.maxsize

for i in range(minus+1):
    cnt = 0
    for j in range(min_len):
        if max_value[i+j] != min_value[j]:
            cnt += 1
    ans = cnt if ans > cnt else ans

if len(A) == len(B):
    cnt = 0
    for j in range(min_len):
        if max_value[j] != min_value[j]:
            cnt += 1
    ans = cnt

print(ans)