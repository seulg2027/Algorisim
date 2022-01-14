# 미로 탐색

from collections import deque

n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
result = [0] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[b].append(a)

def bfs(num):
    q = deque()
    q.append(num)
    visit[num] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visit[i]:
                visit[i] = True
                result[i] = result[v] + 1
                q.append(i)

bfs(a)

if result[b] != 0:
    print(result[b])
else:
    print(-1)