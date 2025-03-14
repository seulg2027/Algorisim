"""
25682번 체스판 다시 칠하기 2
2차원 누적합, 구간합 개념
"""

import sys, copy

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [["0"] * (m + 1)] + list(list("0" + input().strip()) for _ in range(n))
chess_1 = [[0] * (m + 1) for _ in range(n + 1)]
chess_2 = [[0] * (m + 1) for _ in range(n + 1)]
answer = 1e9

# 1) 체스판 다시 칠해야할 부분 1, 놔두는 부분 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if (j % 2 == 0 and i % 2 == 0) or (j % 2 == 1 and i % 2 == 1):
            chess_1[i][j] = 1 if board[i][j] == "B" else 0
            chess_2[i][j] = 1 if board[i][j] == "W" else 0
        else:
            chess_1[i][j] = 0 if board[i][j] == "B" else 1
            chess_2[i][j] = 0 if board[i][j] == "W" else 1

chess_sum1 = copy.deepcopy(chess_1)
chess_sum2 = copy.deepcopy(chess_2)

# 2) 누적합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        chess_sum1[i][j] = chess_sum1[i-1][j] + chess_sum1[i][j-1] - chess_sum1[i-1][j-1] + chess_sum1[i][j]
        chess_sum2[i][j] = chess_sum2[i-1][j] + chess_sum2[i][j-1] - chess_sum2[i-1][j-1] + chess_sum2[i][j]

# 3) 구간합 구하기
for i in range(k, n+1):
    for j in range(k, m+1):
        sum1 = chess_sum1[i][j] - chess_sum1[i][j-k] - chess_sum1[i-k][j] + chess_sum1[i-k][j-k]
        sum2 = chess_sum2[i][j] - chess_sum2[i][j-k] - chess_sum2[i-k][j] + chess_sum2[i-k][j-k]
        answer = sum1 if sum1 < answer else answer
        answer = sum2 if sum2 < answer else answer

print(answer)