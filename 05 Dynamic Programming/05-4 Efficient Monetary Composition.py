# 05-3 효율적인 화폐 구성

# 내가 푼 방법
n, m = map(int, input().split())
coins = []

for i in range(n):
  coins.append(int(input()))

coins.sort(reverse=True)
d = [0] * (m+1)

for i in range(m+1):
  now = i
  for coin in coins:
    # 현재 금액이 동전의 금액보다 큰 경우 반복
    while i >= coin:
      i -= coin
      d[now] += 1
  if i != 0: #0을 못 만드는 경우
    d[now] = -1

print(d[m])

# 답안 예시
n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

# 한 번 계산한 결과를 저장
d = [10001] * (m+1)

# 다이나믹 프로그래밍
d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    # (i-k)원을 만드는 방법이 존재하는 경우
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])