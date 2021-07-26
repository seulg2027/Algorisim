# Q16. 연구소

# 내가 풀려고 시도한 방법
# 막힌 이유 : 벽을 3개 세우는 모든 경우를 구해서, 리스트로 만든 뒤 반복문을 돌렸는데 리스트의 모든 원소가 반영되어서 바이러스 있는 부분을 제외한 모든 영역에 벽이 세워짐... 이걸 해결 못해서 망함
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
laboratory = []

for i in range(n):
  laboratory.append(list(map(int, input().split())))

data = []
virus = []
for i in range(n):
  for j in range(m):
    if laboratory[i][j] == 0:
      data.append((i, j))
    elif laboratory[i][j] == 2:
      virus.append((i, j))

# 벽을 세우는 모든 경우의 좌표를 구함
data = list(combinations(data, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0

def wall_install(cnt):
  for case in data[0]:
    x, y = case
    cnt += 1
    if cnt > 3:
      cnt = 0
      break
    else:
      laboratory[x][y] = 1

wall_install(cnt)


# 답안 예시
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [] # 초기 맵
temp = [[0] * m for _ in range(n)] # 벽을 세운 뒤의 맵

for i in range(n):
  data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2
        virus(nx, ny)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2: # 바이러스가 있는 칸일 경우 퍼져나가게 한다.
          virus(i, j)
    result = max(result, get_score()) # 안전 영역의 크기 
    return
  # 처음에 무조건 이것부터 실행됨 (벽을 세우는 과정) ## 이 부분 헷갈려ㅠ
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        # data에 벽을 세우고 세운 벽을 temp에 옮겨놓은 뒤 data에 있는 벽을 다시 없앤다.
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)