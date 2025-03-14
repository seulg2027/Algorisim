'''
15723번 n단 논법
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
alphabets = []
graph = list([] for _ in range(n*2))

for _ in range(n):
    s = list(input().rstrip().split(" is "))
    for i in range(2):
        if s[i] not in alphabets:
            alphabets.append(s[i])
    graph[alphabets.index(s[0])].append(alphabets.index(s[1]))

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x))
    visited = list(False for _ in range(len(alphabets)))
    visited[x] = True
    
    while q:
        leng, a = heapq.heappop(q)
        if a == y:
            return True
        for i in graph[a]:
            if not visited[i]:
                heapq.heappush(q, (leng+1, i))
                visited[i] = True
    
    return False

for _ in range(int(input())):
    s = list(input().rstrip().split(" is "))
    
    # 전제 조건에 없는 것을 고려해야 함
    if s[0] in alphabets and s[1] in alphabets:
        ans = dijkstra(alphabets.index(s[0]), alphabets.index(s[1]))
    else: ans = False
    print("T" if ans else "F")
