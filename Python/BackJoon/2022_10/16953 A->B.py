# 16953번 A->B

# 되게 구현문제같은데 bfs로 풀리네
# 오랜만에 사부작사부작 푸니까 재밌다

from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
min_value = sys.maxsize

q = deque([(a, 1)])
while q:
  now, cnt = q.popleft()
  case2 = int(str(now) + "1")
  if now * 2 == b or case2 == b:
    min_value = min(min_value, cnt+1)
    break
  if now * 2 < b:
    q.append((now*2, cnt+1))
  if case2 < b:
    q.append((case2, cnt+1))

print(-1) if min_value == sys.maxsize else print(min_value)