'''
4485번 녹색 옷 입은 애가 젤다지?

처음엔 그래프가 아닌데 최단경로 -> DP 생각했다가 케이스 체크해보니 DP로 절대 풀수 없는 것을 깨달음 (규칙이 없다)
다익스트라 / 플로이드 워셜 -> 다익스트라 기기
'''

import sys, heapq
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, distance[0][0]))
    while q:
        x, y, total = heapq.heappop(q)
        if distance[x][y] < total:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = total + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (nx, ny, distance[nx][ny]))
    return distance[-1][-1]

cnt = 1

while True:
    n = int(input())
    if n == 0:
        sys.exit(0)
    answer = "Problem " + str(cnt) + ": "
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[sys.maxsize] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    
    print(answer + str(dijkstra()))
    
    cnt += 1
