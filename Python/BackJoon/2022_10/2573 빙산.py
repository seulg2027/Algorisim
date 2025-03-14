'''
2573번 빙산
처음엔 함수 두개 (1년 후 빙산, 빙산 덩어리 체크용)을 만들어서 구했으나
메모리 초과와 시간초과로.. 한꺼번에 체크하는 함수를 만듦
'''

from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(arr): # 1년 후의 빙산
    q = deque()
    graph = deepcopy(arr)
    visited = [[0]*m for _ in range(n)]
    cnt = 0 # 빙하 개수 체크
    for x in range(n):
        for y in range(m):
            if arr[x][y] >= 1 and not visited[x][y]:
                cnt += 1
                q.append((x,y))
                while q:
                    a, b = q.popleft()
                    visited[a][b] = 1
                    
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] > 0 and not visited[nx][ny]:
                                q.append((nx,ny))
                            if arr[nx][ny] == 0:
                                if graph[a][b] > 0:
                                    graph[a][b] -= 1
    
    return graph, cnt

year = 0
while True:
    graph, ice_cnt = bfs(graph) # 빙산 녹이기
    year += 1
    if ice_cnt == 0: # 만약 빙산이 하나도 없으면..
        print(0)
        break
    elif ice_cnt > 1:
        print(year-1)
        break
