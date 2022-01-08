# 행렬

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0

def change(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      a[i][j] = 1 - a[i][j]

def check():
  for i in range(n):
    for j in range(m):
      if a[i][j] != b[i][j]:
        return False
  return True

# range함수에 마이너스가 들어가면 for 문이 실행이 안된다.
for i in range(n-2):
  for j in range(m-2):
    if a[i][j] != b[i][j]:
      change(i, j)
      cnt += 1

if check():
  print(cnt)
else:
  print('-1')