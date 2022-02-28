# 1484번 다이어트

# 투 포인터로 품

import sys
input = sys.stdin.readline

g = int(input())

numbers = [i*i for i in range(1, g+1)]
left = 0
right = 1
result = []

while right < g:
  num = numbers[right] - numbers[left]
  if num == g:
    result.append(right+1)
    left += 1
  elif num > g:
    left += 1
  elif num < g:
    right += 1

if result:
  for re in result:
    print(re)
else:
  print(-1)