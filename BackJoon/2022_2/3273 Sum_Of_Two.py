# 3273번 두 수의 합

# 투 포인터

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
x = int(input())
left, right = 0, n-1
cnt = 0

while left < right:
  if data[left] + data[right] == x:
    cnt += 1
    right -= 1
  if data[left] + data[right] < x:
    left += 1
  elif data[left] + data[right] > x:
    right -= 1

print(cnt)