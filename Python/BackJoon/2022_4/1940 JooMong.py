# 1940번 주몽

# 투포인터

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
num = list(map(int, input().split()))

num.sort()

left = 0
right = n-1
cnt = 0

while left < right:
  if num[left] + num[right] == m:
    cnt += 1
    left += 1
  if num[left] + num[right] < m:
    left += 1
  elif num[left] + num[right] > m:
    right -= 1

print(cnt)