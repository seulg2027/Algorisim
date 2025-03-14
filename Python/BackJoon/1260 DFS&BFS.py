# DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
  visited_dfs[v] = True
  print(v, end=' ')
  for i in sorted(graph[v]):
    if not visited_dfs[i]:
      dfs(i)

def bfs(v):
  queue = deque([v])
  visited_bfs[v] = True
  while queue:
    state = queue.popleft()
    print(state, end=' ')
    for i in sorted(graph[state]):
      if not visited_bfs[i]:
        queue.append(i)
        visited_bfs[i] = True

dfs(v)
print()
bfs(v)