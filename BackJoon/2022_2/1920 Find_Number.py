# 1920번 수 찾기

# 이분 탐색으로 바로 생각
# 근데 right-1 이 아니고 right = mid - 1 인거 조심

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

def binary_search(x):
  global n
  left = 0
  right = n-1
  while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
      return True
    elif a[mid] >= x:
      right = mid - 1
    elif a[mid] <= x:
      left = mid + 1
  return False

a.sort()

for i in range(m):
  if binary_search(b[i]) == True:
    print(1)
  else:
    print(0)
