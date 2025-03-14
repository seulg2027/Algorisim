# 07-3 Curriculum

################### 문제 정답을 보고 ###################
from collections import deque
import copy

N = int(input())

# 진입차수 초기화
indegree = [0] * (N+1)
# 각 노드에 연결된 간선 정보를 담기 위한 리스트
graph = [[] for _ in range(N+1)]
# 강의 당 수강하는데 걸리는 시간을 담은 리스트
time = [0] * (N+1)

for i in range(1, N+1):
  data = list(map(int, input().split())) # 걸리는 시간, 후수 과목, -1을 차례대로 받음
  time[i] = data[0] # 시간 정보
  # 이 부분이 막혀서 정답 봄...
  for x in data[1:-1]:
    indegree[i] += 1 # 진입차수 추가
    graph[x].append(i) # x에서 

def topology_sort():
  # 내부까지 모두 복사해주는 깊은 복사 사용
  result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque()
  
  # 진입 차수가 0인 노드를 먼저 큐에 삽입
  for i in range(1, N+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    # 큐에서 원소 꺼내기 (진입차수가 낮은 순으로 꺼내지겠지?)
    now = q.popleft()
    for i in graph[now]:
      # 결과값 갱신해주기 (여기서 time 리스트가 갱신되면 안되기 때문에 깊은 복사를 해준거..)
      result[i] = max(result[i], result[now] + time[i])
      # 진입차수 1 빼주기
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
  
  for i in range(1, N+1):
    print(result[i])

topology_sort()