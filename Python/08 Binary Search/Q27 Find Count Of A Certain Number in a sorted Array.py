# Q27 정렬된 배열에서 특정 수 개수 구하기
## 중요 ##

# 처음에는 되게 단순하게 생각해서 품
# 하지만 그게 아니라는 걸 깨달음..

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = 0

def binary_search(data, x, start, end):
  global result
  while start <= end:
    mid = (start+end) // 2
    # 해당 원소일 경우
    if data[mid] == x:
      result += 1
    elif data[mid] <= x:
      start = mid + 1
    elif data[mid] > x:
      end = mid - 1

binary_search(data, x, 0, n-1)

print( result if result > 0 else "-1" )


########### 답안 예시 ###########
# 특정 수의 처음 위치와 마지막 위치를 찾는 코드
# 이 코드... 작동을 안함

# 찾는 수의 처음 위치 찾기
def first(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우!!
  if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우
  elif array[mid] >= target:
    return first(array, target, start, mid - 1)
  else:
    return first(array, target, mid + 1, end)

# 찾는 수의 마지막 위치 찾기
def last(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우
  if (mid == n-1 or target > array[mid + 1]) and array[mid] == target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우
  elif array[mid] >= target:
    return last(array, target, start, mid - 1)
  else:
    return last(array, target, mid + 1, end)

def count_by_value(array, x):
  n = len(array)
  # x가 처음 등장한 인덱스, 마지막으로 등장한 인덱스
  a = first(array, x, 0, n-1)
  b = last(array, x, 0, n-1)
  # 수열에 x가 존재하지 않은 경우
  if a == None or b == None:
    return 0
  return b - a + 1

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

print("-1" if count == 0 else count)


# bisect을 활용한 코드
from bisect import bisect_left, bisect_right

def count_by_value(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index =bisect_left(array, left_value)
  return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x, x)
print("-1" if count == 0 else count)