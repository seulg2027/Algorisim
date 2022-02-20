# 12847번 꿀 아르바이트

# # 투 포인터,, 슬라이딩 윈도우 => 시간초과 해설봄..!

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# money = list(map(int, input().split()))
# max_value = 0

# if m > 0:
#   for start in range(n):
#     if start == n-m+1:
#       break
#     end = start + (m-1)
#     cost = 0
#     for i in money[start:end+1]:
#       cost += i
#     max_value = max(max_value, cost)
  
#   print(max_value)
# else:
#   print(0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = list(map(int, input().split()))

window = sum(money[:m])
answer = window
for i in range(m, n):
  window += money[i] - money[i-m] # window 값을 갱신시켜주는 과정
  answer = max(answer, window)

print(answer)