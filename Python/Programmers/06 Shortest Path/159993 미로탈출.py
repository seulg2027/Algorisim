'''
159993 미로탈출
오랜만에 다익스트라
'''

import heapq
INF = int(1e9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(x, y, maps):
    distance = [[INF] * m for _ in range(n)]
    q = []
    heapq.heappush(q, (0, x, y))
    distance[x][y] = 0
    while q:
        dist, a, b = heapq.heappop(q)
        if distance[a][b] < dist:
            continue
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            cost = dist + 1
            if 0 <= nx < n and 0 <= ny < m:
                if cost < distance[nx][ny] and maps[nx][ny] != "X":
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    return distance

def solution(maps):
    global n, m
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 시작 - 래버, 래버 - 출구 사이의 최소거리를 구하기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                new = dijkstra(i, j, maps)
            if maps[i][j] == "L":
                lx, ly = i, j
                exit = dijkstra(i, j, maps)
            if maps[i][j] == "E":
                ex, ey = i, j
    
    answer = new[lx][ly] + exit[ex][ey] if new[lx][ly] + exit[ex][ey] < INF else -1
    
    return answer