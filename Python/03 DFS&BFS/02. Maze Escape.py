# 02 미로 탈출

# 내가 풀려고 노력한 답
import sys
from collections import deque
input = sys.stdin.readline

n, m =  map(int, input().split())
map_data = []

for i in range(n):
  map_data.append(list(map(int, input().split())))

visited = [[0]*m for i in range(n)]

def escape(x, y):
  queue = deque()
  queue.append((x, y))
  print(queue)
  while queue:
    x, y = queue.popleft()

for i in range(n):
  for j in range(m):
    escape(i, j)


# 정답
import sys
from collections import deque
input = sys.stdin.readline

n, m =  map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

# 상하좌우를 바꿀경우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y)) # 큐에 넣는다.
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 상하좌우 모두 돌아다닌다.
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 만약 그 부분이 범위 밖이거나 벽인경우 무시한다
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue  
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  return graph[n-1][m-1]

print(bfs(0,0))
print(graph)