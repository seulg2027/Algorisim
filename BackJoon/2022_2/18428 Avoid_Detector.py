# 18428번 감시피하기

# # 아이디어가 틀린거같음ㅠㅠ dfs는 맞는데,...

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = []
# detected = [[0] * n for _ in range(n)]
# for _ in range(n):
#   graph += [list(input().split())]

# ans = True

# def dfs(x, y, teacher):
#   if 0 <= x < n and 0 <= y < n: # 예외처리
#     if teacher == 't':
#       detected[x][y] = 1
#       dfs(x-1, y, 'left')
#       dfs(x+1, y, 'right')
#       dfs(x, y-1, 'up')
#       dfs(x, y+1, 'down')
#     else:
#       if graph[x][y] == 'X':
#         detected[x][y] = 1
#         if teacher == 'left':
#           dfs(x-1, y, 'left')
#         elif teacher == 'right':
#           dfs(x+1, y, 'right')
#         elif teacher == 'up':
#           dfs(x, y-1, 'up')
#         elif teacher == 'down':
#           dfs(x, y+1, 'down')
#       elif graph[x][y] == 'S':
#         if teacher == 'left':
#           detected[x+1][y] = 2
#         elif teacher == 'right':
#           detected[x-1][y] = 2
#         elif teacher == 'up':
#           detected[x][y+1] = 2
#         elif teacher == 'down':
#           detected[x][y-1] = 2

# for j in range(n):
#   for i in range(n):
#     if graph[i][j] == 'T':
#       dfs(i, j, 't')

# cnt = 0
# for i in range(n):
#   for j in range(n):
#     if detected[i][j] == 2:
#       if graph[i][j] == 'T':
#         ans = False
#         break
#       cnt += 1

# if cnt == 3 and ans == True:
#   print("YES")
# else:
#   print("NO")


n = int(input())

data = []
teacher = []
wall = []
result = "NO"

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  data.append(list(input().split()))
  for j in range(n):
    if data[i][j] == 'T':
      teacher.append((i, j))

def check_t():
  for t in teacher:
    for i in range(4): # 모든 방향에 대하여
      x, y = t
      while 0 <= x < n and 0 <= y < n:
        if data[x][y] == 'O':
          break
        elif data[x][y] == 'S':
          return False
        x += dx[i]
        y += dy[i]
  return True

def dfs(count):
  global result
  if count > 3:
    return
  if count == 3:
    if check_t() is True:
      result = "YES"
      return
    else:
      result = "NO"
  
  for i in range(n):
    for j in range(n):
      if data[i][j] == 'X':
        data[i][j] = 'O'
        wall.append((i, j))
        dfs(count+1)
        if result == 'YES':
          return
        wall.remove((i, j))
        data[i][j] = 'X'

dfs(0)

print(result)