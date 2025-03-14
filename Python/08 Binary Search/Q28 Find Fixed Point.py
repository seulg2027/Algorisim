# Q28 고정점

# 내가 푼 방법
# 반복문을 두번 돌리는 코드는 피하려고 bisect을 사용함.. 근데 예외가 있음
from bisect import bisect_left

n = int(input())
data = list(map(int, input().split()))
fixed_point = 0 # 고정점 초기화

for index in range(n):
  result = bisect_left(data, index)
  print(result, index)
  # 인덱스와 반환값이 같으면 고정점으로 만들어줌
  if result == index:
    fixed_point = result
    break

print(fixed_point if fixed_point != 0 else "-1")


########### 답안 예시 ###########
def binary_search(array, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == mid:
    return mid
  # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우
  elif array[mid] > mid:
    return binary_search(array, start, mid - 1)
  # 중간점이 큰 경우 오른쪽을 확인
  else:
    return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
  print(-1)
else:
  print(index)