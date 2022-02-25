# 1644번 소수의 연속합

import sys, math
input = sys.stdin.readline

n = int(input())
is_prime = [True for _ in range(n+1)]
is_prime[1] = False

def pick_prime():
  global n
  prime_num = []
  for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i * j <= n:
      is_prime[i*j] = False
      j += 1
  for i in range(1, n+1):
    if is_prime[i]: # 만약 소수이면
      prime_num.append(i)
  return prime_num

prime_num = pick_prime()
l = len(prime_num)
value = 0
prime_sum = []
for i in prime_num:
  value += i
  prime_sum.append(value)

left = 0
right = 1
cnt = 0
while left < l and right < l:
  if prime_sum[right] - prime_sum[left] == n:
    cnt += 1
    right += 1
  elif prime_sum[right] - prime_sum[left] > n:
    left += 1
  elif  prime_sum[right] - prime_sum[left] < n:
    right += 1
if n in prime_sum:
  cnt += 1

print(cnt)