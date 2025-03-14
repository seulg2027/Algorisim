# 1406번 에디터

# 구현..? 시간초과 때문에 애먹음
# 리스트 insert가 append 보다 시간복잡도 훨씬 높음..
# append => O(1) / insert => O(N)

import sys
input = sys.stdin.readline

left = list(input().rstrip())
m = int(input())
right = []

for _ in range(m):
  inst = list(input().split())
  if len(inst) == 2:
    left.append(inst[1])
  else:
    if inst[0] == 'L':
      if len(left) > 0:
        right.append(left.pop())
    elif inst[0] == 'D':
      if len(right) > 0:
        left.append(right.pop())
    elif inst[0] == 'B':
      if len(left) > 0:
        _ = left.pop()

right.reverse()
print("".join(left) + "".join(right))