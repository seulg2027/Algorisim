# 15235번 Olympiad Pizza

# bfs 생각하고 풀이

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pizza = list(map(int, input().split()))
q = deque()

for i in range(n):
  q.append((i, pizza[i]))

time = 0
ans = [0] * n
while q:
  loc, num = q.popleft()
  time += 1
  if num == 1:
    ans[loc] = time
  else:
    q.append((loc, num-1))

for a in ans:
  print(a, end=' ')