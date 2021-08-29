# 떡볶이 떡 만들기

# 내가 푼 방법
# 데이터 정렬을 사용, 반복문 돌림
n, m = map(int, input().split())
data = list(map(int, input().split()))

sort_data = sorted(data, reverse=True)
target = sort_data[0]
result = 0

def search(target):
  global result, m
  # 떡 높이의 총합보다 result값이 작을 때 반복
  while result < m:
    result = 0 # 다시 반복문을 돌때 result 초기화
    target -= 1 # 절단기 높이 줄이기
    for cake in sort_data:
      if cake >= target: # 절단기 높이보다 더 긴 떡일때
        result += (cake - target)
      else: # 더 짧은 떡일 경우 반복문 탈출
        break
  print(target)

search(target)


########### 답안 예시 ###########
# 반복 이진 탐색을 이용해서 구현
# 근데 왜 위에서 한것보다 연산양이 더 많은거같지?

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start<=end):
  total = 0
  mid = (start+end)//2
  for x in array:
    # 잘랐을 때 떡 양 계산
    if x > mid:
      total += x - mid
  # 만약 필요한 떡의 양이 더 많으면 반복문 계속,, 끝점 갱신해줌
  if total < m:
    end = mid -1
  # 아니면 result에 담는다. 시작점이 끝점보다 커지면서 반복문 종료될 것
  else:
    result = mid
    start = mid + 1

print(result)