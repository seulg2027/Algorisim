# 4948번 베스트랑 공준

# 에라토스테네스의 체

import sys, math
input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0:
    break
  num = [True for _ in range(2*n+1)]
  num[1] = False
  for i in range(2, int(math.sqrt(2*n))+1):
    if num[i] == True:
      j = 2
      while i*j <= 2*n:
        num[i*j] = False
        j += 1
  ans = 0
  for i in range(n+1, 2*n+1):
    if num[i] == True:
      ans += 1
  print(ans)
