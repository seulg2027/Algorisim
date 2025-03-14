# 안전 영역


# 내가 푼 풀이
# 이건 런타임 에러^^ 이러다 문제 모든 에러 다 수집하겠네ㅎㅎ
import sys
import copy
sys.setrecursionlimit(1000000)

n = int(input())
height_data = []
for _ in range(n):
  height_data.append(list(map(int, input().split())))

result = []

def search(array, x, y): # dfs 알고리즘
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  if array[x][y] > 0 and array[x][y] != 101: # 비가 내려도 잠기지 않는 영역이면
    array[x][y] = 101 # 표시해두기
    search(array, x+1, y)
    search(array, x-1, y)
    search(array, x, y+1)
    search(array, x, y-1)
    return True
  return False

max_height = 0
for i in range(n):
  for j in range(n):
    max_height = max(max_height, height_data[i][j])

cnt = 0
for height in range(max_height):
  array = copy.deepcopy(height_data)
  for i in range(n):
    for j in range(n):
      array[i][j] = height_data[i][j] - height # 비의 양에 따라 높이 감소
  for i in range(n):
    for j in range(n):
      if search(array, i, j) == True:
        cnt += 1
  result.append(cnt)
  cnt = 0 # 횟수 초기화

print(max(result))