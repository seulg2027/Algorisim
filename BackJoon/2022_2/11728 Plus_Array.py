# 11728번 배열 합치기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

array = a + b

# for i in range(len(array)):
#   min_value = i
#   for j in range(i+1, len(array)):
#     if array[min_value] > array[j]:
#       min_value = j
#   array[i], array[min_value] = array[min_value], array[i]
array.sort()

for item in array:
  print(item, end=' ')