# 17144번 미세먼지 안녕!

# 빡빡구현🐸

import sys, copy
input = sys.stdin.readline

r, c, t = map(int, input().split())
home = []
for _ in range(r):
  home.append(list(map(int, input().split())))

home_copy = copy.deepcopy(home)
cleaner = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def diffusion(x, y):
  diff = home[x][y] // 5
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < r and 0 <= ny < c and home[nx][ny] != -1:
      home_copy[x][y] -= diff
      home_copy[nx][ny] += diff

cnt = 0
while cnt < t:
  # 미세먼지 확산
  for a in range(r):
    for b in range(c):
      if home[a][b] != -1:
        diffusion(a, b)
      else:
        cleaner.append(a)
  # 공기 청정기 작동
  x1, x2, y = cleaner[0], cleaner[1], 0
  tmp1, tmp2 = home_copy[x1][y+1], home_copy[x2][y+1]
  # 오른쪽
  for j in range(2, c):
    pre1 = home_copy[x1][y+j]
    pre2 = home_copy[x2][y+j]
    home_copy[x1][y+j] = tmp1
    home_copy[x2][y+j] = tmp2
    tmp1 = pre1
    tmp2 = pre2
  home_copy[x1][1] = 0
  home_copy[x2][1] = 0
  # 위쪽
  for j in range(x1-1, -1, -1):
    pre1 = home_copy[j][c-1]
    home_copy[j][c-1] = tmp1
    tmp1 = pre1
  # 아래쪽
  for j in range(x2+1, r):
    pre2 = home_copy[j][c-1]
    home_copy[j][c-1] = tmp2
    tmp2 = pre2
  # 왼쪽
  for j in range(c-2, -1, -1):
    pre1 = home_copy[0][j]
    pre2 = home_copy[r-1][j]
    home_copy[0][j] = tmp1
    home_copy[r-1][j] = tmp2
    tmp1, tmp2 = pre1, pre2
  # 아래쪽
  for j in range(x1-2):
    pre1 = home_copy[j][0]
    home_copy[j][0] = tmp1
    tmp1 = pre1
  # 위쪽
  for j in range(r-1, x2-1, -1):
    pre2 = home_copy[j][0]
    home_copy[j][0] = tmp2
    tmp2 = pre2
  home = copy.deepcopy(home_copy)
  cnt += 1

ans = 0
for a in range(r):
  for b in range(c):
    if home_copy[a][b] > 0:
      ans += home_copy[a][b]

print(ans)


## 정답 풀이

# 확산까지는 똑같음
# 공기청정기 로직.. 진짜 천재 아닐까

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if graph[i][0] == -1:
        top = i
        bottom = i + 1
        break


def diffuse():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    diffused = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if graph[x][y] == 0 or graph[x][y] == -1:
                continue

            dust = graph[x][y] // 5

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                    diffused[nx][ny] += dust
                    diffused[x][y] -= dust

    for i in range(r):
        for j in range(c):
            graph[i][j] += diffused[i][j]


def clean_top():
    dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
    x, y, d = top, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == top and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


def clean_bottom():
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    x, y, d = bottom, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == bottom and y == 0:
            break
        if not 0 <= nx < r or not 0 <= ny < c:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


for _ in range(t):
    diffuse()
    clean_top()
    clean_bottom()

print(sum(map(sum, graph)) + 2)