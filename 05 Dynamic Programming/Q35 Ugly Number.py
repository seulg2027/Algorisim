# Q35 못생긴 수

# 내가 푼 방법
# 잘 돌아감
n = int(input())

dp = []

def exists(data, i):
  return (0 <= i < len(data))

for num in range(2000):
  if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    dp.append(num)
  if exists(dp, n-1):
    break

print(dp[n-1])