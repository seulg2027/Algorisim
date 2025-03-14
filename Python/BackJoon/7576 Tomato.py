# 토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato_list = []
riped_tomato = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def check():
  global tomato_list
  is_checked = True
  for i in range(n):
    tomato_list += [list(map(int, sys.stdin.readline().split()))]
    for j in range(m):
      if tomato_list[i][j] == 0:
        is_checked = False
      elif tomato_list[i][j] == 1:
        riped_tomato.append((i, j, 0))
  if is_checked:
    return True
  else:
    return False

result = 0

def bfs(v):
  global result, m, n
  queue = deque(v)
  while queue:
    x, y, day = queue.popleft()
    tomato_list[x][y] = 1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if -1 < nx < n and -1 < ny < m and tomato_list[nx][ny] == 0:
        queue.append((nx, ny, day + 1))
    result = day

if check():
  print(0)
else:
  bfs(riped_tomato)
  for i in range(n):
    for j in range(m):
      if tomato_list[i][j] == 0:
        is_checked = False
        print(-1)
        exit()
  print(result)

##############
## 보완한 코드 ##
##############

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int,input().split())
graph = []
q = deque()

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

bfs()
res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
    res = max(max(graph[i]),res)

print(res - 1)