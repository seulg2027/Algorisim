# 17086번 아기 상어 2

# 5월 마지막날을 장식하는 문제~_~
# 정답률 보고 만만하게 봤다가 문제 이해를 잘못해서 애먹었당 하핳

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
space = []
for i in range(n):
  space.append(list(map(int, input().split())))

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def bfs(a, b):
  global ans
  move = deque([(a, b, 0)])
  visited = [[0] * m for _ in range(n)]
  visited[a][b] = 1
  while move:
    a, b, dist = move.popleft()
    for i in range(8):
      rx = a + dx[i]
      ry = b + dy[i]
      if 0 <= rx < n and 0 <= ry < m and not visited[rx][ry]:
        if space[rx][ry] == 1:
          return dist + 1
        visited[rx][ry] = 1
        move.append((rx, ry, dist+1))
  return dist

ans = 0

for i in range(n):
  for j in range(m):
    if space[i][j] == 0:
      value = bfs(i, j)
      ans = max(value, ans)

print(ans)