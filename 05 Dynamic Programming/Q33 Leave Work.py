# Q33. 퇴사


# 내가 푼 방법
# 예외 처리하다가 시간 다 감
n = int(input())
T = []
P = []

for _ in range(n):
  t, p = map(int, input().split())
  T.append(t)
  P.append(p)

dp = []

# 초깃값 설정
for i in range(T[0]):
  dp.append(P[i])

for i in range(len(dp)):
  if T[i] <= (n-i):
    day = T[i]
    if T[i+day] <= (n-i-day):
      dp[i] += P[i+day]

print(dp)


# 답안 예시
dp = [0] * (n+1)
max_value = 0

for i in range(n-1, -1, -1):
  time = t[i] + i
  if time <= n:
    dp[i] = max(P[i] + dp[time], max_value)
    max_value =dp[i]
  else:
    dp[i] = max_value

print(max_value)