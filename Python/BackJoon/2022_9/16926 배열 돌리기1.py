# 배열 돌리기1

# 돌리기... 아 이거 그전에 카카오 코테에 응용해서 나왔던 거 같은데
# 풀고 나서 보니까 하나도 안비슷함 근데 둘다 어렵다

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

def rotate():
  global x, y, temp
  pre = arr[x][y]
  arr[x][y] = temp
  temp = pre

for _ in range(r): # 원하는 횟수만큼 회전
  for i in range(min(n, m) // 2):
    # x나 y가 고정되어 있어야 한 줄로 돌릴 수 있음
    x = i
    y = i
    temp = arr[x][y] # 비교.. 그 전꺼!
    
    # 왼쪽
    for j in range(i+1, n-i):
      x = j
      rotate()
    # 위쪽
    for j in range(i+1, n-i):
      x = n-j-1
      rotate()
    # 아래쪽
    for j in range(i+1, m-i):
      y = j
      rotate()
    # 오른쪽
    for j in range(i+1, m-i):
      y = m-j-1
      rotate()

for a in range(n):
  for b in range(m):
    print(arr[a][b], end=' ')
  print()
