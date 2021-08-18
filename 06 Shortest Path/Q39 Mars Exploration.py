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
        if next_dist < distance[i[0]][i[1]]:
          distance[i[0]][i[1]] = next_dist
          heapq.heappush(q, (i[0], i[1], next_dist))

  dijkstra()
  print(distance)