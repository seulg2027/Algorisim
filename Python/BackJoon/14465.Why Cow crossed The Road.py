# 14465 소가 길을 건너간 이유5

# 누적 합, 두 포인터, 슬라이딩 윈도우
# pypy로 돌려서 맞음 (python3은 시간초과)

import sys

N, K, B = map(int, sys.stdin.readline().rstrip().split())
data = [1] * (N+1)

for i in range(B):
  data[int(sys.stdin.readline().rstrip())] = 0

broken = 0
min_value = K

for left in range(1, N+1):
  if left > (N - K + 1): # 데이터 검색 끝
    break
  else:
    right = left + K - 1 # right 값 갱신
    for item in data[left:right + 1]:
      if item == 0:
        broken += 1
      if broken >= min_value: # 최솟값보다 크게 나오면 바로 반복문 탈출 
        break
    min_value = min(min_value, broken)
    broken= 0 # 초기화시켜줌

print(min_value)