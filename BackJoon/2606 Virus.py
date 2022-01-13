# 바이러스

n = int(input())
link = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(link):
  l, r = map(int, input().split())
  graph[l].append(r)
  graph[r].append(l)

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(i)

dfs(1)

result = -1
for now in visited:
  if now:
    result += 1

print(result)