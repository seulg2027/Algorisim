'''
3085번 사탕게임

연속된 문자 개수 세기 : groupby('banana')
b ['b']
a ['a']
n ['n']
a ['a']
n ['n']
a ['a']
'''

import sys, copy
from itertools import groupby
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
board_copy = copy.deepcopy(board)

def get_max_candy(graph):
    most_candy_length = 0
    most_candy_color = ''
    for i in range(N):
        for letter, contLetter in groupby(''.join(graph[i])):
            n = len(list(contLetter))
            if n > most_candy_length:
                most_candy_length = n
                most_candy_color = letter
    return most_candy_length, most_candy_color

dx = [1, 0]
dy = [0, 1]

max_value = 0

for i in range(N):
    for j in range(N):
        # 아래, 오른쪽으로 사탕 변경하기
        for d in range(2):
            if 0 <= i+dx[d] < N and 0 <= j+dy[d] < N:
                board_copy[i][j] = board[i+dx[d]][j+dy[d]]
                board_copy[i+dx[d]][j+dy[d]] = board[i][j]
                l1, c1 = get_max_candy(board_copy)
                # 전치행렬 변경하기
                l2, c2 = get_max_candy(list(map(list, zip(*board_copy))))
                max_value = max_value if max(l1, l2) < max_value else max(l1, l2)
                board_copy = copy.deepcopy(board)

print(max_value)