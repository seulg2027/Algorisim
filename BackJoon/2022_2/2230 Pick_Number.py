# 2230번 수 고르기

# 투포인터
# 주의 : m = 0 이고 같은 수를 고를 때
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = []
for _ in range(n):
  numbers.append(int(input()))
numbers.sort()

left = 0
right = 1
ans = sys.maxsize
while left < len(numbers) and right < len(numbers):
  if numbers[right] - numbers[left] >= m:
    ans = min(ans, numbers[right] - numbers[left])
    left += 1
  else:
    right += 1

if m == 0:
  print(0)
else:
  print(ans)
