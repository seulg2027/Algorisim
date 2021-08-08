# 05-1 1로 만들기

# 내가 푼 방법 (테스트 케이스 통과)
# 아직 재귀함수의 틀을 못 벗어난 사람...
x = int(input())

d = [0 for i in range(x + 1)] # 인덱스 1~x까지 사용

for i in range(1, x+1):
  if i % 5 == 0:
    d[i] = 5
  elif i % 3 == 0:
    d[i] = 3
  elif i % 2 == 0:
    d[i] = 2

cnt = 0
min_value = 30000

def makeOne(x):
  global cnt, min_value
  if x == 1:
    min_value = min(min_value, cnt)
  else:
    if d[x] == 5:
      cnt += 1
      makeOne(x//5)
    if d[x] == 0 or d[x-1] == 5:
      cnt += 1
      makeOne(x-1)
    if d[x] == 3:
      cnt += 1
      makeOne(x//3)
    if d[x] == 2:
      cnt += 1
      makeOne(x//2)

makeOne(x)
print(min_value)


# 답안 예시
x = int(input())

# 앞서 계산된 결과를 저장하기 위함
d = [0] * 30001

# 보텀업 방식으로 다이나믹 프로그래밍 진행
# 절대 계산하면서 x의 값을 바꿔서 넘겨줄 생각하지 말자
for i in range(2, x + 1):
  # 1을 빼는 경우를 가장 먼저 고려해줌
  # 왜냐하면 어차피 1을 빼는 경우는 그 전의 수보다 한번 더 계산하게 되므로... 
  # 이걸 처음에 고려하게 되면 계산이 쉽다!
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2] + 1) # 1을 더해주는 이유는 나누면서 계산을 진행했으므로
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5] + 1)

print(d[x])