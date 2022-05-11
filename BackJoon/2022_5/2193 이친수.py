# 2193번 이친수

# 너어어무 기본적인 dp 문제

import sys
input = sys.stdin.readline

n = int(input())
pn = [0] * (n+1)
pn[1] = 1
if n >= 2:
  pn[2] = 1

for i in range(3, n+1):
  pn[i] = pn[i-2] + pn[i-1]

print(pn[n])