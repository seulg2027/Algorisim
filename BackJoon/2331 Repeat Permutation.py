# 2331번 반복 순열

import sys
input = sys.stdin.readline

a, p = map(int, input().split())
nums = [a]

while True:
  temp = 0
  for i in str(nums[-1]):
    temp += (int(i) ** p)
  if temp in nums:
    idx = nums.index(temp)
    break
  nums.append(temp)

print(idx)