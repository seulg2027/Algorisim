# 5014번 스타트링크

# dp와 bfs개념을 합쳐서 푼 문제!!
# heapq도 이건 안됨.. 메모이제이션이 필요
# heapq 이나 bfs는 그 전의 값과 비교할 수 없다는거 잊지말기

from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]

def bfs(start):
    global F, G, U, D
    q = deque([(start, 0)])
    visited[start] = 1
    while q:
        now, cost = q.popleft()
        if now+U <= F and not visited[now+U]:
            q.append((now+U, cost+1))
            ans[now+U] = min(ans[now+U], ans[now] + 1)
            visited[now+U] = 1
        if now-D >= 1 and not visited[now-D]:
            q.append((now-D, cost+1))
            ans[now-D] = min(ans[now-D], ans[now] + 1)
            visited[now-D] = 1

ans = [sys.maxsize for _ in range(F+1)]
ans[S] = 0
bfs(S)
if ans[G] == sys.maxsize:
    print("use the stairs")
else:
    print(ans[G])
