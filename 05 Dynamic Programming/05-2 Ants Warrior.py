# 05-2 개미 전사

# 내가 푼 방법
N = int(input())
data = list(map(int, input().split()))
result = 0
cnt = 0

def findFood(data, result):
  global cnt
  if cnt == N//2:
    return result
  else:
    max_value = max(data)
    max_index = data.index(max_value)
    if data[max_index+1] == -1 or data[max_index-1] == -1: # 앞 뒤 식량이 이미 없는 경우
      data[max_index] = -2 # 식량을 못먹게 함
      findFood(data, result)
    else: # 앞, 뒤에 식량이 없는 경우
      cnt += 1
      data[max_index] = -1
      findFood(data, result + max_value)

findFood(data, result)
print(result)


# 답안 예시
n = int(input())
array = list(map(int, input().split()))

# DP테이블 초기화
d = [0] * 100

# 배열 
d[0] = array[0]
# 리스트 0, 1 중에서 더 큰 걸 고른다.
d[1] = max(array[0], array[1])

for i in range(2, n):
  # d[i-3]은 d[i-1]과 d[i-2]를 구하는 과정에서 이미 고려가 되어있음.
  d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])