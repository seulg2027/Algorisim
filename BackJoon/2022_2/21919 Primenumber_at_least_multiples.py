# 21919번 소수 최소 공배수

# 에라토스테네스의 체로 풀이
# 주의 : 중복된 수가 주어질 경우

import sys, math
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers_set = list(set(numbers))
numbers = sorted(numbers_set)
is_prime = [True for _ in range(numbers[-1]+1)]
is_prime[1] = False

for i in range(2, int(math.sqrt(numbers[-1]))+1):
  j = 2
  while i*j <= numbers[-1]:
    is_prime[i*j] = False
    j += 1

ans = 1
for i in numbers:
  if is_prime[i]:
    ans *= i

print(ans) if ans > 1 else print(-1)