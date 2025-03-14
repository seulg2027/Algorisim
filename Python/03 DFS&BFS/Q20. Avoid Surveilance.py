# Q20. 감시 피하기

# 연구소 문제와 비슷한거같은데 다름
# 연구소는 재귀함수로 바이러스가 계속 퍼져나갔지만 이건 아니다
# 테스트 케이스 통과

# 연구소 문제에서 방향을 정해주고 + 리스트를 하나 더 만들어줌으로써 장애물을 만났을 때 감시를 할 수 없게 만듦
import sys
input = sys.stdin.readline

n = int(input())
passageway = []
surveil = [[0]*n for i in range(n)] # 감시할 수 있는 칸을 계산한 맵
data = [[0]*n for i in range(n)]

for i in range(n):
  passageway.append(list(input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def surveil_arrange(dir, x, y): # 감시하기, 데이터를 바꿈
  if dir == 4: #방향이 정해져있지 않고 모든 방향을 검사해야하는 경우
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < n :
        if data[nx][ny] != 2:
          data[nx][ny] = 1
          surveil_arrange(i, nx, ny)
  else: # 방향이 정해져 있는 경우
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx >= 0 and nx < n and ny >= 0 and ny < n :
      if data[nx][ny] == 2:
        return
      else:
        data[nx][ny] = 1
        surveil_arrange(dir, nx, ny)

result = 0

def surveil_avoid():
  global result
  for i in range(n):
    for j in range(n):
      if passageway[i][j] == 'S':
        if data[i][j] != 1:
          result = 1

def dfs(cnt):
  global data, result
  if cnt == 3: # 장애물 세개 설치할 곳을 모두 찾았다면?
    for i in range(n):
      for j in range(n):
        if passageway[i][j] == 'O':
          surveil[i][j] = 2 # 장애물 설치
          data[i][j] = 2
        elif passageway[i][j] == 'X' or passageway[i][j] == 'S':
          surveil[i][j] = 0 # 아무것도 없음
          data[i][j] = 0
        elif passageway[i][j] == 'T':
          surveil[i][j] = 1 # 감시자 배치
          data[i][j] = 1
    for i in range(n):
      for j in range(n):
        if surveil[i][j] == 1:
          surveil_arrange(4, i, j)
    surveil_avoid()
    return
  # 장애물 설치
  for i in range(n):
    for j in range(n):
      if passageway[i][j] == 'X':
        passageway[i][j] = 'O'
        cnt += 1
        dfs(cnt)
        passageway[i][j] = 'X'
        cnt -= 1

dfs(0)
print("YES" if result==1 else "NO")


############################ 답안 예시 #############################
# 조합으로 구현
from itertools import combinations

n = int(input())
board = [] # 복도 맵 정보 (전체 정보)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 빈 공간 위치 정보

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i, j))
    if board[i][j] == 'X':
      spaces.append((i, j))

# 특정 방향으로 감시하는 함수,,
# 나랑 다른 점! 나는 먼저 감시할 수 있는 위치를 확인한 뒤 => 학생이 그 감시거리에 들어와 있는가 확인했지만
# 최대한 for문을 적게 사용하기 위해 한꺼번에 계산한 걸루 보임
def watch(x, y, direction):
  # 왼쪽 방향으로 감시
  if direction == 0:
    while y >= 0:
      if board[i][j] == 'S':
        return True
      if board[i][j] == 'O':
        return False
      y -= 1
  # 오른쪽 방향 감시
  if direction == 1:
    while y < n :
      if board[i][j] == 'S':
        return True
      if board[i][j] == 'O':
        return False
      y += 1
  if direction == 2:
    while x >= 0:
      if board[i][j] == 'S':
        return True
      if board[i][j] == 'O':
        return False
      x -= 1
  if direction == 3:
    while x >= 0:
      if board[i][j] == 'S':
        return True
      if board[i][j] == 'O':
        return False
      x += 1
  return False

# 장애물 설치 이후 학생이 감지되는지 검사
def process():
  for x, y in teachers:
    for i in range(4):
      if watch(x, y, i): # 만약 감지되면('S'의 데이터가 있을 때 True값을 반환)
        return True
  return False

find = False # 학생이 한명도 감지되지 않도록 설치할 수 있는지 여부

for data in combinations(spaces, 3):
  for x, y in data:
    board[x][y] = 'O'
  if not process(): #감지되지 않으면
    find = True
    break
  for x, y in data:
    board[x][y] = 'X'

if find:
  print("YES")
else:
  print("NO")