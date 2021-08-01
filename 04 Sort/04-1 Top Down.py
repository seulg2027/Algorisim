# 위에서 아래로

# 내가 푼 방법 (예시 이용)
n = int(input())
array = []

for i in range(n):
  array.append(int(input()))

for i in range(n):
  max_index = i
  for j in range(i+1, n):
    if array[max_index] < array[j]:
      max_index =j
  array[i], array[max_index] = array[max_index], array[i]

for i in range(n):
  print(array[i], end=' ')

# 라이브러리 이용하면..
array = sorted(array, reverse=True)