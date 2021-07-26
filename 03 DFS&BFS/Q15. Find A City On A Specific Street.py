# Q15. 특정 거리의 도시 찾기


# 내가 푼 방법
# 시간 초과,.,, 하지만 테스트 케이스 통과 ><
# 백준 사이트에서는 런타임에러🤔
import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
data = [[] for i in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  data[a].append(b)

cnt = 0
result_dir = [300001 for _ in range(n+1)]

def bfs(x, cnt):
  queue = deque()
  queue.append(data[x])
  while queue:
    v = queue.popleft()
    cnt += 1
    if not v:
      result_dir[x] = min(result_dir[x], cnt)
    else:
      for i in v:
        result_dir[i] = min(result_dir[i], cnt)
      for i in v:
        if data[i]: # 그 원소에 관해 길이 더 존재할 경우
          for item in data[i]:
            bfs(item, cnt)
        else: # 길이 존재하지 않으면,,
          cnt = 0

bfs(x, cnt)

res_list = [i for i, value in enumerate(result_dir) if value == k]

if res_list:
  for i in res_list:
    print(i)
else:
  print(-1)


# 답안 예시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x])
while q:
  now = q.popleft()
  for next_node in graph[now]: # 현재 도시에서 이동할 수 있는 모든 도시 확인(가장 기초적인 방법!!)
    if distance[next_node] == -1: # 방문하지 않은 도시이면
      distance[next_node] = distance[now] + 1
      q.append(next_node)

check = False
for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check =True

if check == False:
  print(-1)