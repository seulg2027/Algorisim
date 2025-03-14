# 제곱 ㄴㄴ수

# 다이나믹 프로그래밍으로 풀려고 시도
# 혼자 테케 시도해본건 다 통과했는데 메모리 초과ㅠ ㅜㅠㅠㅠ
# dp 배열 수 때문에 메모리 초과 나는 듯... 주어진 수가 너무 커
import sys

min_value, max_value = map(int, sys.stdin.readline().rstrip().split())
dp = [0] * (max_value - min_value + 1)

# 제곱 수를 갱신시켜주는 함수
def is_squared(x):
  for i in range(2, x+1):
    if i**2 > x: # 더 큰 수면 제곱수를 갱신시켜줄 필요가없음
      break
    dp[i**2 - min_value] = 1 # 제곱 수를 갱신시켜준다.

is_squared(max_value)

result = 0
squared = []

for i in range(min_value, max_value + 1):
  if dp[i - min_value] == 1: # 제곱 수일 경우
    squared.append(i)
  else: # 제곱 수가 아닐 경우
    for j in range(len(squared)):
      if i % squared[j] == 0: # 나누어 떨어지는 경우
        dp[i - min_value] = 2 # 2를 넣어준다
        break # 반복문 끝(제곱 수 맞음)
    if dp[i - min_value] == 0: # 제곱수로 나누어 떨어지지 않는경우
      result += 1

print(result)


## 구글링해서 나온 코드
# 에라토스테네스의 체를 활용한 코드
# https://youjeonghan.github.io/baekjoon/1016_Squared_nono_number/
# 이해가 안감 계속 봐야겠다,,

min, max = map(int, input().split())
validate = [1 for i in range(max-min+1)] # 초기값은 모두 1
cnt=0
i=2
while i**2 <= max: # max값이 i의 제곱수보다 큰 경우 반복
  mul = min // i**2
  while mul * (i**2) <= max: 
    if mul * (i**2) - min >= 0 and mul * (i**2) - min <= max - min: # 나누어 떨어지는지?
      validate[mul * (i**2) - min] = 0 # 나누어 떨어지면 0으로 만들어준다.
    mul +=1
  i +=1

print(sum(validate))