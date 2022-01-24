# 기타 레슨

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

minlesson = max(lessons)
sumlesson = sum(lessons)
ans = int(1e9)

while minlesson <= sumlesson:
  mid = (minlesson + sumlesson) // 2
  cnt = 0
  sum_num = 0
  for i in range(len(lessons)):
    if sum_num + lessons[i] > mid:
      cnt += 1
      sum_num = 0
    sum_num += lessons[i]
  if sum_num:
    cnt += 1
  
  if cnt > m:
    minlesson = mid + 1
  else:
    ans = min(ans, mid)
    sumlesson = mid - 1

print(ans)