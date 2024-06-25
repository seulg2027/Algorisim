'''
67259번 경주로 건설

최고로 어려운 BFS였다.. 까다로운 조건의 구현 + BFS
'''
from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dist = [[int(1e9)] * n for _ in range(n)]
    corner = [[0] * n for _ in range(n)]
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque([(0, 0, 0, -1, 0)]) # x, y, 비용, 이전 방향, corner 개수
    dist[0][0] = 0
    
    while q:
        x, y, price, d, cnt = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1: continue
                
                # 첫 start라면
                if d == -1:
                    dist[nx][ny] = price+100
                    corner[x][y] = cnt
                    q.append((nx, ny, price+100, i, cnt))
                # 이전 방향과 같고, 거리 갱신 가능할 때
                elif d == i and price+100 <= dist[nx][ny]:
                    dist[nx][ny] = price+100
                    corner[x][y] = cnt
                    q.append((nx, ny, price+100, i, cnt))
                # 이전 방향과 다르고, 거리 갱신 가능할 때
                elif d != i and price+600 <= dist[nx][ny]:
                    dist[nx][ny] = price+600
                    corner[x][y] = cnt+1
                    q.append((nx, ny, price+600, i, cnt+1))
                # 이전 방향과 다르고, 거리 갱신이 불가하더라도 코너 개수가 이전보다 더 적은 경로인 경우 -> 따져봐야 함
                elif d != i and corner[nx][ny] > cnt+1:
                    if (corner[nx][ny] - cnt+1) * 500 > price+600 - dist[nx][ny]:
                        dist[nx][ny] = price+600
                        corner[x][y] = cnt+1
                        q.append((nx, ny, price+600, i, cnt+1))
    
    answer = dist[-1][-1]
    
    return answer