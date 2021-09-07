# 동전1

# 처음 문제를 보고 재귀 함수로 풀어야겠다는 생각을 했음
# dp문제의 정석...

# 내가 푼 풀이
n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]

coin.sort(reverse=True)
cnt = []
for i in range(n):
  cnt.append(k//coin[i]) # 최대로 넣을 수 있는 경우 구하기
print(cnt)

result = 0 # 경우의 수 반영하는 변수
m = 0

def coin_value(start, value):
  global result, k, m
  if value == 0:
    result += 1
    value = k
  if value >= 0:
    if start == n:
      start = 0
    if coin[start] <= value:
      if cnt[start] == 0: # 횟수가 0일 경우
        print("코인", coin[start])
      else:
        cnt[start] -= 1 # 횟수 차감
        coin_value(start + 1, value - coin[start])
        cnt[start] += 1

coin_value(0, k)
print(result)


# 다른 사람 풀이,,, 외우자

n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1 # 초깃값 꼭 설정해주기

for i in coin:
  for j in range(i, k+1):
    if (j-i) >= 0:
      dp[j] += dp[j-i]

print(dp[k])