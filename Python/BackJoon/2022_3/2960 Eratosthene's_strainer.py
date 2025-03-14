# 2960번 에라토스테네스의 체

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = [True for _ in range(n+1)]
cnt = 0

for i in range(2, n+1):
  j = 1
  while i*j <= n:
    if numbers[i*j] == True:
      cnt += 1
    numbers[i*j] = False
    if cnt == k:
      print(i*j)
      exit() # 이게 없으면 cnt가 같을 경우 모든 경우의 수 출력
    j += 1