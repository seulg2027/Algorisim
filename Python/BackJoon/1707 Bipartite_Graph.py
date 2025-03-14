# 1707번 이분 그래프

# bfs로 품

from collections import deque
import sys
input = sys.stdin.readline

def bfs(q):
  while q:
    st, now = q.popleft()
    visited[now] = 1
    for i in graph[now]:
      if not visited[i]:
        state[i] = 1 if st == 0 else 0
        q.append((state[i], i))

for _ in range(int(input())):
  v, e = map(int, input().split())
  graph = [[] for _ in range(v+1)]
  state = [-1 for _ in range(v+1)]
  visited = [0 for _ in range(v+1)]
  
  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  ans = True
  # bfs를 통해 state 값 갱신
  # 그래프가 모두 연결되어있다는 보장이 없으므로 bfs도 하나하나 다 해줘야함
  for i in range(1, v+1):
    if not visited[i]:
      state[i] = 0
      bfs(deque([(state[i], i)]))
  
  # state 
  for i in range(1, v+1):
    for j in graph[i]:
      if state[i] == state[j]:
        ans = False
  
  print("YES") if ans == True else print("NO")