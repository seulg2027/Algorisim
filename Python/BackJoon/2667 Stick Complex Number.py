# 2667번 단지번호 붙이기

import sys
input = sys.stdin.readline

n = int(input())
complex = []
for _ in range(n):
  complex += [list(map(int, input().rstrip()))]

homes = 0
answer = []

def cnt_complex(x, y):
  global homes
  if 0 <= x < n and 0 <= y < n:
    if complex[x][y] == 1:
      complex[x][y] = 0
      homes += 1
      cnt_complex(x-1, y)
      cnt_complex(x+1, y)
      cnt_complex(x, y-1)
      cnt_complex(x, y+1)
      return True
  return False

cnt = 0
for i in range(n):
  for j in range(n):
    if cnt_complex(i, j) == True:
      answer.append(homes)
      cnt += 1
      homes = 0

print(cnt)
answer.sort()
for ans in answer:
  print(ans)