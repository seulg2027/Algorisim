'''
구슬 탈출 2
1. 빨간 구슬 굴리기 (벽, 구멍까지 굴리기)
2. 파란 구슬 굴리기 (벽, 구멍까지 굴리기)
3. R O, B X 일 경우에만 횟수 출력 / R X, B X 일 경우 한 번 더 굴리기
    => 파란 구슬이 구멍에 빠졌을 경우 -1 출력
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(n))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

red, blue = [0, 0], [0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            board[i][j] = '.'
            red = [i, j]
        if board[i][j] == 'B':
            board[i][j] = '.'
            blue = [i, j]

def roll_bead(x, y, arrow, a, b):
    nx = x + dx[arrow]
    ny = y + dy[arrow]
    if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] == 'O':
            return nx, ny
        elif board[nx][ny] == '#' or (nx == a and ny == b):
            return x, y
        elif board[nx][ny] == '.':
            result = roll_bead(nx, ny, arrow, a, b)
            return result
    else:
        return -1, -1

q = deque([(red, blue, 0)])

while q:
    red_n, blue_n, cnt = q.popleft()
    # print(red_n, blue_n, cnt)
    if cnt >= 10:
        break
    
    for i in range(4):
        if (red_n[1] == blue_n[1] and red_n[0] > blue_n[0] and i == 2) or (red_n[0] == blue_n[0] and red_n[1] > blue_n[1] and i == 0) or (red_n[0] == blue_n[0] and red_n[1] < blue_n[1] and i == 1) or (red_n[1] == blue_n[1] and red_n[0] < blue_n[0] and i == 3):
            rx, ry = roll_bead(red_n[0], red_n[1], i, blue_n[0], blue_n[1])
            bx, by = roll_bead(blue_n[0], blue_n[1], i, rx, ry)
        else:
            bx, by = roll_bead(blue_n[0], blue_n[1], i, red_n[0], red_n[1])
            rx, ry = roll_bead(red_n[0], red_n[1], i, bx, by)
        
        if (rx == -1 and ry == -1) or (bx == -1 and by == -1):
            continue
        
        if board[rx][ry] == 'O' and board[bx][by] != 'O':
            print(cnt + 1)
            sys.exit(0)
        elif board[rx][ry] == '.' and board[bx][by] == '.':
            q.append([[rx, ry], [bx, by], cnt + 1])

print(-1)