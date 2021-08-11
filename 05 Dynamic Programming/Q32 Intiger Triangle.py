# Q32 정수 삼각형

# 내가 푼 방법
n = int(input())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(i+1):
    # 오른쪽 위
    if j == i:
      right_up = 0
    else:
      right_up = data[i-1][j]
    # 왼쪽 위
    if j == 0:
      left_up = 0
    else:
      left_up = data[i-1][j-1]
    data[i][j] = data[i][j] + max(left_up, right_up)

print(max(data[n-1]))