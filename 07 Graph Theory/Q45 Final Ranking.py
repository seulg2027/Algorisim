# Q45 최종 순위


# 내가 푼 방법
# 틀렸는데 예외를 못찾겠음..
from collections import deque

def topology_sort(N):
  result = []
  q = deque()
  # 위상 정렬으로 초기값 설정
  for i in range(1, N+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1 # 진입차수 차감
      if indegree[i] == 0:
        q.append(i)
  
  # 만약 정렬된 결과의 길이가 N이면 그대로 순서 나열
  if len(result) == N:
    result.reverse()
    for i in result:
      print(i, end=' ')
  else: # 정렬된 결과로 찾지 못하면 ? 출력
    print("?")

for _ in range(int(input())):
  N = int(input())
  # 이전의 순위 받는 리스트
  data = list(map(int, input().split()))
  # 그래프 초기화
  graph = [[] for _ in range(N+1)]
  # 진입차수 초기화
  indegree = [0] * (N+1)
  for i in range(1, N):
    for j in range(i):
      graph[data[i]].append(data[j])
      indegree[data[j]] += 1
  
  M = int(input())
  # 연산이 가능한지 체크해주는 변수
  is_possible = True
  for i in range(M):
    a, b = map(int, input().split())
    if b in graph[a]: # 만약 b원소가 지금 그래프에 들어있다면 연산 실행
      graph[a].remove(b)
      indegree[b] -= 1
      graph[b].append(a)
      indegree[a] += 1
    else: # 아니라면 false반환(impossible)
      is_possible = False
  
  if is_possible:
    topology_sort(N)
  else:
    print("IMPOSSIBLE")