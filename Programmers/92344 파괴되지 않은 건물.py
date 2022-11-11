'''
92344번 파괴되지 않은 건물
처음에 무지성으로 구현으로 품 (효율성테스트 통과 못합)
=> 누적합으로 시간복잡도 O(1)
'''
# 내가 푼 코드
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    while skill:
        tp, r1, c1, r2, c2, degree = skill.pop(0)
        if skill == []:
            answer = 0
        if tp == 1:
            degree = -degree
        
        for i in range(n):
            for j in range(m):
                if r1 <= i <= r2 and c1 <= j <= c2:
                    board[i][j] += degree
                if board[i][j] > 0:
                    try: answer += 1
                    except: continue
    return answer

# 누적합 코드
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    tmp = [[0] * (m+1) for _ in range(n+1)]
    answer = 0
    
    for type, r1, c1, r2, c2, degree in skill:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    for i in range(n): # 행 기준 누적합
        for j in range(m):
            tmp[i][j + 1] += tmp[i][j]
    
    for j in range(m): # 열 기준 누적합
        for i in range(n):
            tmp[i + 1][j] += tmp[i][j]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0: answer += 1
    
    return answer