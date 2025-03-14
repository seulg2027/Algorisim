# 2096번 내려가기

# dp 로 바로 풀었는데,, 메모리 초과나서 copy 이용해서 품

import sys, copy
input = sys.stdin.readline

n = int(input())
graph = []
min_graph = []
for i in range(n):
  if i == 0:
    graph.append(list(map(int, input().split())))
    min_graph = copy.deepcopy(graph)
    continue
  else:
    new_list = list(map(int, input().split()))
    # 리스트 copy안써주면 요소가 완전 같이 바뀌어버리는거 주의
    update = copy.deepcopy(new_list)
    graph.append(new_list)
    min_graph.append(update)
    
    graph[1][0] += max(graph[0][0], graph[0][1])
    graph[1][1] += max(graph[0][0], graph[0][1], graph[0][2])
    graph[1][2] += max(graph[0][1], graph[0][2])
    
    min_graph[1][0] += min(min_graph[0][0], min_graph[0][1])
    min_graph[1][1] += min(min_graph[0][0], min_graph[0][1], min_graph[0][2])
    min_graph[1][2] += min(min_graph[0][1], min_graph[0][2])
    
    del graph[0]
    del min_graph[0]

print(max(graph[0]), min(min_graph[0]))