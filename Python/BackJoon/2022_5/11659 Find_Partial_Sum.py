# 11659번 구간 합 구하기 4

# 구간 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
value = 0
partial_sum = [0]

for num in nums:
  value += num
  partial_sum.append(value)

for i in range(m):
  start, end = map(int, input().split())
  print(partial_sum[end] - partial_sum[start-1])