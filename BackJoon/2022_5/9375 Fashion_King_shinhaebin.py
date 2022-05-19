# 9375번 패션왕 신해빈

# 백트래킹까지 고려했으나,, 그냥 연산 구현 문제였음

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  clothes = dict()
  
  for i in range(n):
    a, kind = input().split()
    try:
      clothes[kind] += 1
    except:
      clothes[kind] = 1
  ans = 1
  for key in clothes:
    ans *= clothes[key] + 1 
  
  print(ans-1)

