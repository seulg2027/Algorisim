# 1


# 채점 반도 못 통과함
id_list = ["con", "ryan"]
report = 	["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

from collections import deque

result = [0] * len(id_list)

def topology_sort(graph, indegree, n, k):
  q = deque()
  for i in range(1, n):
    if indegree[i] >= k: # 신고횟수를 넘어가는
      q.append(i) # 아이디 넣기
  while q:
    now = q.popleft()
    for i in graph[now]: # 정지먹은 아이디가 있는 곳 순환
      result[id_list.index(i)] += 1 # 신고 횟수 늘리기
  return result

def solution(id_list, report, k):
  alert_cnt = [0] * len(id_list)
  graph = [[] for _ in range(len(id_list))]
  for group in report:
    alerting, alerted = group.split('')
    if alerting in graph[id_list.index(alerted)]: # 동일한 사람이 신고할 경우 예외처리
      continue
    else:
      graph[id_list.index(alerted)].append(alerting)
      alert_cnt[id_list.index(alerted)] += 1 # 진입차수 증가
  answer = topology_sort(graph, alert_cnt, len(id_list), k)
  return answer

solution(id_list, report, k)