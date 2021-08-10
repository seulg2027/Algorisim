# Q32 정수 삼각형

# 내가 푼 방법
n = int(input())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

dp = []
index = 1
result = data[0][0]

for i in range(1, n):
  index += 1
  for j in range(0, index):
    result += max(data[i][j], data[i][j+1])

print(dp)