# 11559 뿌요뿌요

from collections import deque
import sys, copy
input = sys.stdin.readline

field = []
visited = [[0]*6 for _ in range(12)]
for i in range(12):
  field.append(list(input().rstrip()))
field.reverse()
ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def drop():
  global field, visited
  visited = [[0]*6 for _ in range(12)]
  for i in range(1, 12):
    for j in range(6):
      if field[i][j] != '.' and field[i-1][j] == '.':
        for k in range(i):
          if field[k][j] == '.':
            field[k][j] = field[i][j]
            field[i][j] = '.'
            break

def bumb(color):
  global field, visited
  cnt = 0
  field2 = copy.deepcopy(field)
  visited2 = copy.deepcopy(visited)
  while q:
    x, y = q.popleft()
    visited2[x][y] = 1
    field2[x][y] = '.'
    cnt += 1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < 12 and 0 <= ny < 6:
        if not visited2[nx][ny] and field[nx][ny] == color:
          q.append((nx, ny))
  if cnt >= 4:
    field = copy.deepcopy(field2)
    return True
  else:
    visited = copy.deepcopy(visited2)
    return False

while True:
  array = []
  for i in range(12):
    for j in range(6):
      if field[i][j] != '.' and not visited[i][j]:
        q = deque([(i, j)])
        t = bumb(field[i][j])
        array.append(t)
  if True in array:
    ans += 1
    drop()
  if array == [] or not True in array:
    break

print(ans)