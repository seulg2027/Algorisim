'''
6593번 상범 빌딩
'''

import sys
from collections import deque
input = sys.stdin.readline

dl = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 0, 1, 0, -1]
dc = [0, 0, 1, 0, -1, 0]

def bfs(l, r, c):
    visited = list(list([False] * C for _ in range(R)) for _ in range(L))
    q = deque([(0, l, r, c)])
    visited[l][r][c] = True
    
    while q:
        cnt, sl, sr, sc = q.popleft()
        if building[sl][sr][sc] == 'E':
            return cnt
        
        for i in range(6):
            nl = dl[i] + sl
            nr = dr[i] + sr
            nc = dc[i] + sc
            # 빌딩 안이어야 함, 금이 있는 자리면 피함
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
                if not visited[nl][nr][nc] and building[nl][nr][nc] != '#':
                    q.append((cnt+1, nl, nr, nc))
                    visited[nl][nr][nc] = True
    return -1

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        exit(0)
    
    building = []
    
    for _ in range(L):
        building.append(list(list(input().rstrip()) for _ in range(R)))
        input()
    
    for l in range(L):
        for r in range(R):
            for c in range(C):
                # 상범이의 위치에서 출발
                if building[l][r][c] == 'S':
                    ans = bfs(l, r, c)
                    if ans == -1:
                        print("Trapped!")
                    else:
                        print(f"Escaped in {ans} minute(s).")
