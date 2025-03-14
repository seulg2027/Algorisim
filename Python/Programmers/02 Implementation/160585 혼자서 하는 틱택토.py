'''
160585번 혼자서 하는 틱택토

틱택토 문제는 너무 조건이 까다로워ㅠㅠ
'''

def solution(board):
    answer = -1
    
    def get_bingo(dx, dy):
        for c in range(1, 3):
            nx, ny = i + dx*c, j + dy*c
            if 0 <= nx < 3 and 0 <= ny < 3:
                if board[i][j] != board[nx][ny]:
                    return 0
        return 1
    
    X = 0
    O = 0
    bingo = [0, 0]
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.': continue
            
            ans = 0
            if i == 0 and j == 0:
                ans += get_bingo(1, 1)
            if i == 2 and j == 0:
                ans += get_bingo(-1, 1)
            if i == 0:
                ans += get_bingo(1, 0)
            if j == 0:
                ans += get_bingo(0, 1)
            
            if board[i][j] == 'O':
                bingo[0] += ans
                O += 1
            elif board[i][j] == 'X':
                bingo[1] += ans
                X += 1
    
    # O, X 개수가 1, 0개 차이
    if (O - X) not in [0, 1] or O > 5 or X > 4:
        answer = 0
    # 승자가 1명이어야 함 / X가 빙고 1초과면 안됨
    elif 0 not in bingo or bingo[1] > 1:
        answer = 0
    elif bingo[1] == 1 and (O - X) == 0:
        answer = 1
    elif bingo[0] == 0 and bingo[1] == 0:
        answer = 1
    elif bingo[0] in (1, 2) and (O - X) == 1:
        answer = 1
    else:
        answer = 0
    
    return answer