# Q21. 인구 이동


# 내가 푼 방법
#
# 예외 처리를 못함.. 그러니까 오픈된 국경을 가진 사람끼리 다같이 인구 공유하는 무지 멋진 상황이 연출됨
# 이런ㅠㅠㅠㅠㅠ n=2인 테스트 케이스에 국한해서 성립되는 식을 만들어 버리다니
from itertools import combinations

N, L, R = map(int, input().split())

data = [] # 2차원 리스트
data_list = [] # 1차원 리스트
is_opened = [] # 열린 국경만 담음

for i in range(N):
  data.append(list(map(int, input().split())))

def opened_border():
  for i in range(N):
    for j in range(N):
      data_list.append(data[i][j])

calculation = 0
result = 0

def invest_opened(population):
  for x, y in population: # 두 개의 인구 조합 중에,,
    if abs(x-y) >= L and abs(x-y) <= R: # L이상 R이하를 구함
      for i in range(N):
        for j in range(N):
          if data[i][j] == x or data[i][j] == y:
            if (i, j) not in is_opened:
              is_opened.append((i, j))
  if is_opened:
    return True
  else:
    return False


def dfs(data):
  cnt = 0
  global calculation, result
  opened_border()
  population = list(combinations(data_list, 2))
  value = invest_opened(population)
  if value == True:
    for x, y in is_opened:
      calculation += data[x][y]
      cnt += 1
    calculation = calculation // cnt
    for x, y in is_opened:
      data[x][y] = calculation # 새로운 인구 배정
    result += 1
    is_opened.clear()
    data_list.clear() #리스트를 깨끗하게 만들어준 뒤
    dfs(data)
  else : # 조건에 만족하는 것이 없을 시
    return # 종료

dfs(data)

print(result)

# 답안 예시
from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

# 특정 위치에서 출발 -> 모든 연합을 체크한 뒤 갱신
def process(x, y, index):
  # (x, y)의 위치와 연결된 나라 정보를 담는 리스트
  united = []
  united.append((x, y))
  # Bfs를 위한 큐 자료구조 정의
  q = deque()
  q.append((x, y))
  union[x][y] = index
  summary = graph[x][y]
  count = 1
  while q:
    x, y = q.popleft() # 현재 가지고 있는 큐
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        if 1 <= abs(graph[nx][ny] - graph[x][y] <= r):
          q.append((nx, ny))
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx, ny))
  for i, j in united:
    graph[i][j] = summary // count
  return count

total_count = 0

while True:
  union = [[-1]*n for _ in range(n)]
  break