# 4796 캠핑

import sys
input = sys.stdin.readline

t = []

while True:
  L, P, V = map(int, input().split())
  
  if L == 0 and P == 0 and V == 0:
    for i in range(len(t)):
      value1 = (t[i][2] // t[i][1]) * t[i][0]
      value2 = t[i][2] % t[i][1]
      if value2 < t[i][0]:
        ans = value1 + value2
      else:
        ans = value1 + t[i][0]
      print("Case "+ str(i+1) + f": {ans}")
    break
  else:
    t.append([L, P, V])

