# Q17 경쟁적 전염


# 내가 푼 방법
# 막힌 이유 : 바이러스 종류 순대로 리스트에 추가시켜서 2차원리스트를 만들었는데,,, 덱의 2차원 리스트 원소를 뽑을 때 망했다..
# 2차원 리스트 원소를 뽑아서 popleft시켜야하는데 그걸 못하겠어.
# 덱에는 왠만하면 2차원리스트를 넣지 말자. 1차원만 넣고.. 2차원으로 만든건 참조만합시다ㅠ
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
data = []

for i in range(n):
  data.append(list(map(int, input().split())))

s, q_x, q_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
List = [[] for i in range(k+1)]

def data_input():
  for i in data:
    for virus_sort in i:
      if virus_sort != 0 :
        x = data.index(i)
        y = i.index(virus_sort)
        List[virus_sort].append((x, y))# 종류별로 데이터를 담는다, 낮은 번호의 바이러스가 먼저 증식해서

q = deque()

def dfs(s, cnt, q_x, q_y):
  if not q: #큐가 비어있다면 데이터를 담는다
    data_input()
  q.append(List)
  print(q)
  while s >= cnt: # 시간이 다 되기 이전까지는 호출가능함
    if s == cnt:
      print(data[q_x - 1][q_y - 1])
      return
    while q:
      nowlist = q.popleft()
      print(nowlist)
      cnt += 1
      for now in nowlist: # 바이러스 하나마다 검사해보기
        if now == []:
          continue
        x, y = now[0]
        q.popleft()
        print(q)
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          # 만약 범위를 벗어나지 않았다면 한칸씩
          if nx >= 0 and nx < n and ny >= 0 and ny < n:
            data[nx][ny] = data[x][y]
      print('갯수 :'+str(cnt))
      dfs(s, cnt, q_x, q_y)

dfs(s, 0, q_x, q_y)


# 답안 예시
# 나랑 엄청 비슷하게 생각했는데 덱을 잘 다뤘다...ㅎ 그 점이 다름
# 똑같이 리스트에 먼저 데이터를 담고 덱에 옮겨담았는데 왜
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보
data = [] # 바이러스 정보

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 위치 (시간을 빼먹었다는게 포인트군..)

data.sort()
q = deque(data)
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(q)
while q:
  virus, s, x, y = q.popleft() #아 ㅠㅠㅠㅠㅠ
  if s == target_s: 
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus # 바이러스 종류를 넣는다
        q.append((virus, s+1, nx, ny)) # 큐에 넣음으로써 다음 순서에 검사하도록한다. s를 더해서 시간을 늘리고!

print(graph[target_x -1][target_y -1])