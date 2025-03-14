# # 1697번 숨바꼭질

# # dfs 풀이 - 메모리 초과 / 시간 초과...

# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

# n, k = map(int, input().split())
# idx = max(n, k)
# graph = [[] for _ in range(200001)]
# visited = [0 for _ in range(200001)]

# for i in range(1, idx*2+1):
#   graph[i].extend([i-1, i+1, i*2])

# cnt = 0
# ans = []

# def dfs(v):
#   global cnt
#   if v == k:
#     ans.append(cnt)
#   for now in graph[v]:
#     if 0 < now < idx*2+1:
#       if not visited[now]:
#         visited[now] = 1
#         cnt += 1
#         dfs(now)
#         cnt -= 1
#         visited[now] = 0

# dfs(n)
# print(min(ans))


# bfs 정답코드 참고해서 다시 풀기,,

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = set()
q = deque([(n, 0)])
if n==k:
  print(0)
  exit(0)

while q:
  v, t = q.popleft()
  a = [2*v, v+1, v-1] # 우선순위 : 2*v => v+1 => v-1
  for way in a:
    if way == k: # 위치가 같을 경우
      print(t + 1)
      q.clear()
      break
    # 범위 밖으로 벗어났거나 이미 방문한 곳이면
    if way in visited or way < 0 or way > 100000:
      continue
    else:
      q.append((way, t+1))
      visited.add(way)