# Q29 공유기 설치

# 내가 푼 방법
# 분명 잘 돌아가는데...?
# 답지보고 첫번째 집에만 공유기 설치하고, 마지막 집에는 설치하고 시작하는게 아니라는 걸 깨달음

import sys
input = sys.stdin.readline()

N, C = map(int, input().split())

home = [] # 집의 위치
for i in range(N):
  home.append(int(input()))
home.sort()

modem = []

def install_modem(home, N, start, end):
  global C
  # 첫번째 집과 마지막 집에는 무조건 공유기 설치
  modem.append(start)
  modem.append(end)
  C -= 2
  # 설치해야할 공유기가 있을 경우 반복
  while C > 0:
    mid = (start+end) // 2
    if (mid -1) == start:
      modem.append(mid)
      # 시작점, 끝점 초기화
      start = mid
      end = N-1
      C -= 1
    elif (mid+1) == end:
      modem.append(mid)
      end = mid
      start = 0
      C -= 1
    # 인접한 거리가 더 큰 집을 이진탐색
    elif home[mid] - home[start] > home[end] - home[mid]:
      end = mid + 1
    else :
      start = mid - 1

install_modem(home, N, 0, N-1)
modem.sort()

# 가장 인접한 거리 구하기
min_value = home[modem[1]] - home[modem[0]]
for i in range(len(modem) - 1):
  min_value = min(min_value, home[modem[i+1]] - home[modem[i]])

print(min_value)


########### 답안 예시 ###########
n, c = list(map(int, input().split(' ')))

array = []
for i in range(N):
  array.append(int(input()))
array.sort()

# start, end를 최소 최대 거리로 잡아야 함! 그냥 위치로 하면 이상하게 나옴
start = 1 # 최소거리
end = array[-1] - array[0] # 가능한 최대 거리
result = 0

while(start <= end):
  mid = (start + end) // 2
  value = array[0]
  count = 1
  # 현재의 mid값을 이용해 공유기를 설치
  for i in range(1, n):
    # 중간값보다 현재 값이 크면 value 갱신(중간값을 옮겨줌)
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count >= c: #c개 이상 공유기를 설치할 수 있는 경우
    start = mid + 1
    result = mid
  else: #c개 이상 공유기를 설치할 수 없는 경우
    end = mid - 1

print(result)