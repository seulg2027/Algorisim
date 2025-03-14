# 11000 강의실 배정

# 정렬, 자료구조

import sys, heapq
input = sys.stdin.readline

n = int(input())
subject = [list(map(int, input().split())) for _ in range(n)]
subject.sort(key=lambda x: x[0])

classes = []

for i in range(n):
  if classes:
    if classes[0] <= subject[i][0]:
      heapq.heappop(classes)
  heapq.heappush(classes, subject[i][1])

print(len(classes))