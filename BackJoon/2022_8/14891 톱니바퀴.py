# 14891번 톱니바퀴

import sys
input = sys.stdin.readline

saw = []
for i in range(4):
  saw.append(list(map(int, input().rstrip())))
method = []
n = int(input())
for _ in range(n):
  method.append(list(map(int, input().split())))

# 회전하는 함수
def rotate(setting, dir):
  if dir == 1: # 시계 방향인 경우
    s = setting.pop()
    setting.insert(0, s)
  else: # 시계 반대 방향인 경우
    s = setting.pop(0)
    setting.append(s)
  return setting

# 해당 톱니바퀴를 회전시킬지 말지 확인하는 함수
def rotate_check(x, y):
  if 0 <= x < 4 and 0 <= y < 4:
    if saw[x][2] == saw[y][6]:
      return False
    else:
      return True
  else:
    return None


for i in range(n):
  is_rotated = [0] * 4 # 회전시킬지 여부
  now = method[i][0]-1
  is_rotated[now] = 1 # 회전하는 톱니바퀴
  direction = [0] * 4
  direction[now] = method[i][1] # 회전 방향
  d1 = [-1, 1, -1, 1]
  d2 = [1, -1, 1, -1]
  if direction[now] == d1[now]:
    direction = d1
  else:
    direction = d2
  
  # 회전하는지 여부
  for j in range(1, 4): 
    if rotate_check(now-j, now-j+1) == True:
      is_rotated[method[i][0]-j-1] = 1
    else:
      break
  for j in range(1, 4):
    if rotate_check(now+j-1, now+j) == True:
      is_rotated[method[i][0]+j-1] = 1
    else:
      break
  for k in range(4):
    if is_rotated[k] == 1:
      rotate(saw[k], direction[k])

ans = 0
for s in range(4):
  if saw[s][0] == 1:
    ans += 2 ** s
print(ans)
