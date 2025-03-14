# 알고 스팟

# 뭘로 풀어야할지 헷갈려서 dfs, bfs와 최단경로를 따로 공부하고 품
# 다시보니 다익스트라로 풀어야할 것 같아서 다익스트라 ㄱ
import heapq

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(m)] # 이거 sys.stdin.readline() 으로 안되더라...

INF = int(1e9)
distance = [[INF] * n for _ in range(m)] # 최단 경로

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
q =[(graph[x][y], x, y)] # 초기값 설정
# 최단 경로 초기화 해줌
distance[x][y] = graph[x][y] # 시작 노드 = 초기값
while q:
  dist, x, y = heapq.heappop(q) # 힙 이용해서,, 다익스트라
  if distance[x][y] < dist: # 이미 방문했던 노드라면
    continue # 무시한다
  for i in range(4): # 네가지 방향으로 검사
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= m or ny < 0 or ny >= n: # 범위를 벗어나면 무시
      continue
    cost = dist + graph[nx][ny] # 현재 비용 + 그 다음 비용
    if cost < distance[nx][ny]: # 계산한 비용이 현재 기록된 비용보다 작으면 갱신, 힙에 넣어줌
      distance[nx][ny] = cost
      heapq.heappush(q, (cost, nx, ny))

print(distance[m-1][n-1])