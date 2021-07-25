# 01 음료수 얼려먹기

# 내가 푼 방법
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
shape_data = []

for i in range(n):
  shape_data.append(list(map(int, input().split())))

ice_count = 0

def data_test(shape_data, x, y, ice_count):
  if x > m or x < 0 or y > n or y < 0:
    return 0
  else:
    if shape_data[x][y] == 0:
      shape_data[x][y] = 1
      if shape_data[x][y+1] == 1 and shape_data[x+1][y] == 1: # 아니야.. 이렇게 세면 안 돼
        ice_count += 1
      return 1
    return 0

for i in range(n):
  for j in range(m):
    result = data_test(shape_data, i, j, ice_count)

print(ice_count)


# 정답

## 제일 중요한 것 : 얼음 틀의 0 묶음을 모두 센 다음 result에 추가하는 부분,,,
def dfs(x, y):
  if x <= -1 or x >=m or y <= -1 or y >= m:
    return False
  if shape_data[x][y] == 0:
    shape_data[x][y] = 1
    # 상, 하, 좌, 우 모두 0인지 검사
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    # 0을 모두 1로 만든 뒤 true 반환
    return True
  # 만약 1이면
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)
