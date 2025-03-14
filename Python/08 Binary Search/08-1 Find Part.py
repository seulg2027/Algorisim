# 부품 찾기


# 내가 푼 방법
# 이진 탐색 (반복문)을 이용하여 코드를 구현 #
N = int(input())
part = list(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

def binary_search(part, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if part[mid] == target:
      # 찾았다면 True 반환
      return True
    elif part[mid] > target:
      end = mid - 1
    elif part[mid] <= target:
      start = mid + 1
  # 만약 못찾았다면
  return False

part.sort()

for i in range(M):
  if binary_search(part, target[i], 0, N-1) == True:
    print("yes", end=' ')
  else:
    print("no", end=' ')


########### 계수 정렬을 사용한 소스코드 ###########

n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 받아서 기록
for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print("no", end=' ')


########### 집합 자료형을 사용한 소스코드 ###########

n = int(input())
# 전체 부품 번호를 입력받아서 집합자료형에 중복없이 기록
set_array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  # 집합에 있다면
  if i in set_array:
    print('yes', end=' ')
  else:
    print("no", end=' ')