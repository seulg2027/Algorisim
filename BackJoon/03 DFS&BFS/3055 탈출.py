'''
3055번 탈출

문제에서 준대로 충실하게 구현하면 됨
'''

from collections import deque
import sys, copy
input = sys.stdin.readline

r, c = map(int, input().split())
soup_map = list(list(input().rstrip()) for _ in range(r))
cp_soup_map = copy.deepcopy(soup_map)
visited = [[False] * c for _ in range(r)]
start = [0, 0]
dest = [0, 0]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 물 이동
def flush():
    for i in range(r):
        for j in range(c):
            if soup_map[i][j] == '*':
                for k in range(4):
                    ni = dx[k] + i
                    nj = dy[k] + j
                    if 0 <= ni < r and 0 <= nj < c:
                        if soup_map[ni][nj] != '*' and soup_map[ni][nj] != 'D' and soup_map[ni][nj] != 'X':
                            cp_soup_map[ni][nj] = '*'
    return cp_soup_map

# 고슴도치 이동
def go_destination(x, y):
    global soup_map, cp_soup_map
    q = deque([(x, y, 0)])
    visited[x][y] = True
    now_t = 0
    while q:
        a, b, t = q.popleft()
        if a == dest[0] and b == dest[1]:
            return t
        
        if now_t != t:
            soup_map = copy.deepcopy(flush())
            now_t = t
        
        if soup_map[a][b] == '*': # 물이 덮칠 곳은 가지 않는다.
            continue
        
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny] and soup_map[nx][ny] in ['.', 'D']:
                    q.append((nx, ny, t+1))
                    visited[nx][ny] = True
    return -1

for i in range(r):
    for j in range(c):
        if soup_map[i][j] == 'S':
            start = [i, j]
        if soup_map[i][j] == 'D':
            dest = [i, j]

result = go_destination(start[0], start[1])

print("KAKTUS" if result == -1 else result)