# 16397번 탈출

# # dfs 인줄 알고 dfs로 풀었으나,,, 재귀 깊이 초과로 실패 n이 너무 큼

# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(10**9)

# n, t, g = map(int, input().split())
# cnt = 0
# result = []
# inf = 100000

# def make_num(num):
#   if num*2 >= inf:
#     return inf
#   str_num = str(num*2)
#   s = str(int(str_num[0]) - 1)
#   ans = str_num[1:]
#   if s != 0:
#     ans = s + ans
#   return int(ans)

# visited = [0 for _ in range(inf)]

# def dfs(s, cnt):
#   if s < 0:
#     return
#   if cnt == t or s == g:
#     if s == g:
#       result.append((cnt, s))
#     return
#   if s+1 < inf and not visited[s+1]:
#     visited[s+1] = 1
#     dfs(s+1, cnt+1)
#     visited[s+1] = 0
#   num = make_num(s)
#   if num < inf and not visited[num]:
#     visited[num] = 1
#     dfs(num, cnt+1)
#     visited[num] = 0

# dfs(n, 0)

# if result:
#   result.sort()
#   print(result[0][0])
# else:
#   print("ANG")

# bfs 코드

import sys
from collections import deque
input = sys.stdin.readline

n, t, g = list(map(int, input().split()))
INF = 100000

def bfs(start):
  q = deque()
  visit = [0 for _ in range(INF)]
  q.append((start, 0))
  visit[start] = 1
  
  while q:
    here, cost = q.popleft()
    if cost > t: # 현재까지 시도 횟수가 주어진 시도 횟수보다 많은 경우
      return "ANG"
    if here == g: # 정답과 같은 경우
      return cost
    # A, B 버튼 누른 경우 둘다 큐에 넣어준다.
    # A 버튼을 누른 경우
    if here + 1 < INF and not visit[here+1]:
      q.append((here+1, cost+1))
      visit[here+1] = 1
    # B 버튼을 누른 경우
    if here*2 < INF:
      temp = str(here*2)
      if int(temp) != 0:
        temp = str(int(temp[0]) - 1) + temp[1:]
      temp = int(temp)
      if not visit[temp]:
        q.append((temp, cost+1))
        visit[temp] = 1
  return "ANG"

ans = bfs(n)
print(ans)