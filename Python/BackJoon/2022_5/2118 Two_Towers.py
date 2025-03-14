# 2118번 두 개의 탑

# 두개.. 투포인터 생각

# import sys
# input = sys.stdin.readline

# n = int(input())
# sum_circle = 0
# circle = []
# for _ in range(n):
#   a = int(input())
#   circle.append(a)
#   sum_circle += a
# dist = 0

# for left in range(n-1):
#   right = n - 1
#   outer_value = sum(circle[:left+1])
#   inner_value = sum_circle - outer_value
#   dist = max(dist, min(outer_value, inner_value))
#   while left < right-1:
#     right -= 1
#     inner_value -= circle[right]
#     outer_value += circle[right]
#     dist = max(dist, min(inner_value, outer_value))

# print(dist)

# 시간초과 나서 구간합으로 변경

import sys
input = sys.stdin.readline

n = int(input())
sum_circle = 0
circle = []
for _ in range(n):
  a = int(input())
  sum_circle += a
  circle.append(sum_circle)

dist = 0

for left in range(n-1):
  right = n - 1
  while left < right:
    value1 = circle[right] - circle[left]
    value2 = sum_circle - value1
    dist = max(dist, min(value1, value2))
    right -= 1

print(dist)