# 1806번 부분합

# 투포인터 while문 사용할 때 left, right 맨 마지막에 더할것!

# while True
# right가 n에 도달했을 경우,, 그런데 반복문 맨 위에 배치하지 않은 이유는
# right += 1을 마지막에 진행하기 때문에 마지막 요소까지 범위를 확인해 볼 수 있게 하기 위해서!

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
left, right = 0, 0
min_value = sys.maxsize
sum_value = 0

while True:
  if sum_value >= s:
    min_value = min(min_value, right-left)
    sum_value -= data[left]
    left += 1
  
  elif right == n:
    break
  elif sum_value < s:
    sum_value += data[right]
    right += 1

if min_value == sys.maxsize:
  print(0)
else:
  print(min_value)