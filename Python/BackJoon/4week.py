# # 기타 레슨

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# lessons = list(map(int, input().split()))

# minlesson = max(lessons)
# sumlesson = sum(lessons)
# ans = int(1e9)

# while minlesson <= sumlesson:
#   mid = (minlesson + sumlesson) // 2
#   cnt = 0
#   sum_num = 0
#   for i in range(len(lessons)):
#     if sum_num + lessons[i] > mid:
#       cnt += 1
#       sum_num = 0
#     sum_num += lessons[i]
#   if sum_num:
#     cnt += 1
  
#   if cnt > m:
#     minlesson = mid + 1
#   else:
#     ans = min(ans, mid)
#     sumlesson = mid - 1

# print(ans)

# # 게임 

# X, Y = map(int, input().split())
# Z = (Y * 100) // X

# if X >= 99:
#   print(-1)
# else:
#   answer = 0
#   left = 1
#   right = X
  
#   while left <= right:
#     mid = (left + right) // 2
#     if ((Y + mid) * 100 // (X + mid)) <= Z:
#       left = mid+1
#     else:
#       answer = mid
#       right = mid - 1
  
#   print(answer)

# # 숫자 카드 2

# import sys
# from bisect import bisect_right, bisect_left
# input = sys.stdin.readline

# n = int(input())
# cards = list(map(int, input().split()))
# m = int(input())
# data = list(map(int, input().split()))

# cards.sort()

# def binary_search(arr, left_value, right_value):
#   right_index = bisect_right(arr, right_value)
#   left_index = bisect_left(arr, left_value)
#   return right_index - left_index

# result_list = []

# for i in range(m):
#   result = binary_search(cards, data[i], data[i])
#   result_list.append(result)

# for j in range(m):
#   print(result_list[j], end=' ')

# 제곱근

import sys
input = sys.stdin.readline

n = int(input())

def binary_search(target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if mid ** 2 == target:
      return mid
    elif mid ** 2 > target:
      end = mid - 1
    else:
      start = mid + 1

print(binary_search(n, 0, n // 2 - 1))