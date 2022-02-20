# 2003번 수들의 합2

# 전형적인 투 포인터 문제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
end = 0
cnt = 0
sum_num = 0

for start in range(n):
  while sum_num < m and end < n:
    sum_num += num[end]
    end += 1
  if sum_num == m:
    cnt += 1
  sum_num -= num[start]

print(cnt)