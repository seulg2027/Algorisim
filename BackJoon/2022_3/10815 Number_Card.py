# 10815번 숫자 카드

# 보자마자 이분탐색 ㄱㄱ

import sys
input = sys.stdin.readline

n = int(input())
sanggun = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
sanggun.sort()

def search(x):
  left = 0
  right = n-1
  while left <= right: # 같을 경우를 꼭 포함하고 있어야함
    mid = (left+right) // 2
    if sanggun[mid] == x:
      return True
    elif sanggun[mid] > x:
      right = mid - 1
    elif sanggun[mid] < x:
      left = mid + 1
  return False

for card in cards:
  if search(card) == True:
    print(1, end=' ')
  else:
    print(0, end=' ')