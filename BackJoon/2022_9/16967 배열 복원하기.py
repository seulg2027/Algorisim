# 16967번 배열 복원하기

# 차근차근 케이스를 나눠서 풀어보자!

import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
graph = []
a_arr = [[0] * w for _ in range(h)] # a 배열
visited = [[0] * w for _ in range(h)] # a 배열 완성
layout = [[0] * (w+y) for _ in range(h+x)] # 겹친 횟수

for _ in range(h+x):
  graph.append(list(map(int, input().split())))

for i in range(h):
  for j in range(w):
    layout[i][j] += 1
    layout[i+x][j+y] += 1

# 겹치지 않는 경우
def no_overlap():
  for i in range(h+x):
    for j in range(w+y):
      if layout[i][j] == 1:
        if i >= h or j >= w:
          a_arr[i-x][j-y] = graph[i][j]
          visited[i-x][j-y] = 1
        else:
          a_arr[i][j] = graph[i][j]
          visited[i][j] = 1

# 겹치는 경우
def overlap(a, b):
  a_arr[a][b] = graph[a][b] - a_arr[a-x][b-y]

no_overlap()
for a in range(h):
  for b in range(w):
    if visited[a][b] == 0:
      overlap(a, b)
    print(a_arr[a][b], end=' ')
  print()
