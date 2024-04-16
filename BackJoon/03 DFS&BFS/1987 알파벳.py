'''
1987번 알파벳


'''

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = list(list(input().rstrip()) for _ in range(r))
visited = [[0] * c for _ in range(r)]
answer = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, alphas):
    global answer
    is_done = True
    
    answer = max(len(alphas), answer)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
            if board[nx][ny] not in alphas:
                is_done = False
                alphas += board[nx][ny]
                visited[nx][ny] = 1
                dfs(nx, ny, alphas)
                visited[nx][ny] = 0
                alphas = alphas[:-1]
    
    if is_done:
        return

visited[0][0] = 1
dfs(0, 0, board[0][0])

print(answer)