# 13305 주유소


# 내가 푼 풀이
# 먼저 덱을 사용해야겠다고 생각
from collections import deque

n = int(input())
value = list(map(int, input().split()))
station = list(map(int, input().split()))

i = -1
fee = 0
result = 0
q = deque(station[0:n-1])
while q:
  now_value = q.popleft()
  if q: # 큐가 안비었으면
    next_value = q.popleft()
    i += 1
    fee += value[i]
    if now_value >= next_value:
      result += now_value * fee
      fee = 0 # 다시 초기화 해줌
      q.appendleft(next_value)
    else:
      q.appendleft(now_value)
  else:
    fee += value[n-2]
    result += now_value * fee

print(result)