# 바닥 공사

# 내가 푼 방법
N = int(input())

d = [0] * (N+1)
d[1] = 1
d[2] = 3

for i in range(N+1):
  # 타일을 크게 가로 크기가 2, 1인 타일로 나눔
  num2 = i // 2
  num1 = i % 2
  if num1 == 1:
    # num1 + num2 => 타일을 배치하는 경우의 수, -1은 겹치는 경우의 수
    d[i] = (d[2] ** num2) * (num1 + num2) - 1
  else:
    d[i] = (d[2] ** num2)

print(d[N])


# 답안 예시
n = int(input())

d = [0]*1001
d[1] = 1
d[2] = 3

for i in range(3, n+1):
  d[i] = (d[i-1] + 2 * d[i-2]) % 796796 #에에엥엥ㅇ......이거 뭐지

print(d[n])