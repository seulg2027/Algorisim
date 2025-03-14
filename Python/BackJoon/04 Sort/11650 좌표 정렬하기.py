'''
11650번 좌표 정렬하기
기본 정렬
'''

import sys
input = sys.stdin.readline

N = int(input())

num_list = list(list(map(int, input().split())) for _ in range(N))
num_list.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(f"{num_list[i][0]} {num_list[i][1]}")
