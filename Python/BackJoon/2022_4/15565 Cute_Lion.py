# 15565 귀여운 라이언

# 투포인터

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dolls = list(map(int, input().split()))
lion = []
cnt = 0

for i in range(n):
  if dolls[i] == 1:
    lion.append(i)
    cnt += 1

if cnt < k:
  print(-1)
else:
  start = 0
  end = k-1
  ans = n
  
  while end < len(lion):
    size = lion[end]-lion[start]+1
    if ans > size:
      ans = lion[end]-lion[start]+1
    start += 1
    end += 1
  
  print(ans)
