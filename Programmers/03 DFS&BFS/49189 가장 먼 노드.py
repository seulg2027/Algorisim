'''
49189번 가장 먼 노드
'''

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([(1, 1)])
    visited[1] = 1
    max_lv = 0
    while q:
        now = q.popleft()
        ## 가장 Lv 높은 노드이면 answer 1 더하기, Lv이 더 높으면 answer 초기화하기
        if max_lv < now[1]:
            max_lv = now[1]
            answer = 1
        elif max_lv == now[1]:
            answer += 1
        
        for j in graph[now[0]]:
            if not visited[j]:
                visited[j] = 1
                q.append((j, now[1]+1))
    
    return answer