# Q39 화성 탐사

# 내가 푼 방법
# 테스트 케이스만큼 반복
# 왜 틀렸는지 진짜...모르겠음ㅠ_ㅜ
import heapq
INF = int(1e9)

for _ in range(int(input())):
  N = int(input())
  data = []
  for i in range(N):
    data.append(list(map(int, input().split())))

  # 2차원 그래프 만들어줌
  graph = [[[]*N] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if i-1 >= 0:
        graph[i-1][j].append((i, j, data[i][j]))
      if j-1 >= 0:
        graph[i][j-1].append((i, j, data[i][j]))

  distance = [[INF] * N for _ in range(N)]
  print(graph)

  # 0,0 부터 N-1, N-1까지 중 최단 경로
  def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, data[0][0]))
    distance[0][0] = data[0][0] # 처음 거리
    while q:
      x, y, dist= heapq.heappop(q)
      if distance[x][y] < dist:
        continue
      for i in graph[x][y]:
        next_dist = distance[x][y] + i[2]
        if next_dist < distance[i[0]][i[1]]: # 아직 실행 안했을 때 
          distance[i[0]][i[1]] = next_dist
          heapq.heappush(q, (i[0], i[1], distance[i[0]][i[1]]))

  dijkstra()
  print(distance[N-1][N-1])


########################## 답안 예시 ##########################


import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())):
  n = int(input())
  graph = []
  for i in range(n):
    graph.append(list(map(int, input().split())))
  
  distance = [[INF] * n for _ in range(n)]
  #### 여기까진 같음
  
  x, y = 0, 0
  q =[(graph[x][y], x, y)]
  distance[x][y] = graph[x][y]
  while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
      continue
    # 아 이거 bfs에서 맨날 봤던,,, 그런 형태인데
    # 근데 왜 4번이나 돌리지..? 두번만 돌려도 되지 않나
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      # 현재 노드 비용 + 그다음 노드로 이동하는 비용
      cost = dist + graph[nx][ny]
      if cost < distance[nx][ny]:
        distance[nx][ny] = cost
        heapq.heappush(q, (cost, nx, ny))
  
  print(distance[n-1][n-1])