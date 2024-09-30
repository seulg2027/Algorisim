'''
모든 방향으로 이동 가능하기 때문에 DP 아님
-> DP는 방향이 정해져있음

다익스트라
'''

import sys
import heapq
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = 0

while True:
    n = int(input())
    t += 1
    if n == 0:
        sys.exit(0)
    
    square = list(list(map(int, input().split())) for _ in range(n))
    cost = list([1e9] * n for _ in range(n))
    
    q = []
    heapq.heappush(q, [square[0][0], 0, 0]) # 거리, x, y
    cost[0][0] = square[0][0]
    while q:
        dist, x, y = heapq.heappop(q)
        if cost[x][y] < dist:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n and cost[nx][ny] > dist + square[nx][ny]:
                heapq.heappush(q, [dist + square[nx][ny], nx, ny])
                cost[nx][ny] = dist + square[nx][ny]
    
    print(f"Problem {t}: {cost[-1][-1]}")

