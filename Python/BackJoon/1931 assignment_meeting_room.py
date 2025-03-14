# 회의실 배정

import sys

n = int(sys.stdin.readline())

data = []
sorted_start = sorted([list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)],key=lambda x:(x[0],x[1]))
sorted_end = sorted(sorted_start, key=lambda x: x[1])

end_value = 0
result = 0

for idx in range(n):
  if idx == 0:
    result += 1
    end_value = sorted_end[idx][1]
  else:
    if end_value <= sorted_end[idx][0]:
      result += 1
      end_value = sorted_end[idx][1]

print(result)