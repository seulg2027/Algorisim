# 1092번 배

# bfs로 풀이

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
clane = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

clane.sort(reverse=True)
boxes.sort(reverse=True)

if clane[0] < boxes[0]:
  print(-1)
else:
  ship = deque([])
  ans = 0
  
  while boxes:
    ans += 1
    for i in range(n):
      for j in range(len(boxes)):
        if clane[i] >= boxes[j]:
          ship.append(boxes[j])
          del boxes[j]
          break
  print(ans)