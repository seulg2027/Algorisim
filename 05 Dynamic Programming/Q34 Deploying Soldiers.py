# Q34 병사 배치하기


# 내가 풀려고 시도한 방법,, 
N = int(input())
data = list(map(int, input().split()))

dp = [0] * 2000

for i in range(N):
  index = i
  for j in range(i+1, N):
    if data[index] < data[j]:
      dp[index] += 1

# 모두 정렬될 때까지 실행됨
cnt = 0

def df():
  global cnt
  result = 1
  max_dp = max(dp)
  print(max_dp)
  data.remove(max_dp)
  for i in range(N):
    for j in range(i+1, N):
      if data[i] < data[j]: # 만약 더 큰 데이터가 뒤에 있다면
        result = 0
        cnt += 1
        df()
  if result == 1: # 더이상 더 큰 데이터가 없다면 중단
    return

df()

print(cnt) # 답은 나오는데 인덱스 초과 에러가 뜸ㅠ_ㅜ


###################################   답안 예시    ###################################

# 문제 아이디어가 진짜,,, 너무 난해함ㅠㅠㅠㅠㅠㅠ 외우자

n = int(input())
array = list(map(int, input().split()))
array.reverse() #순서를 뒤집어서 ** 증가하는 부분 중 가장 긴 수열 ** 문제로 전환

# 1차원 dp 테이블 초기화
dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))