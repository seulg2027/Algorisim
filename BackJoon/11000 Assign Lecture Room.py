# 강의실 배정


# 내가 푼 답

## 로직 => 받은 강의실을 덱에 넣어서 같은 강의실끼리 리스트로 만들어 준 후, 앞 뒤 강의실과 시간이 겹치는지 봄
## 시간이 겹치는 강의실이 있으면 false, 없으면 true
## false 이고 다음 비교할 강의실이 없으면 강의실 추가해주고
## false 이고 다음 강의실이 있으면 그 강의실에 대해 다시 search
## true 이면 그 강의실에 배정

# 결과는 시간초과🤪
import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()
lecture_room = 0

def assign(k):
  global lecture_room
  sortList = list(filter(lambda x: (x[0] == k), q)) # 강의실 대로 필터링
  idx = True
  for item in sortList:
    if not (item[2] <= s or item[1] >= s): # 조건을 만족하지 못할 경우
      idx = False
    if sortList.index(item) + 1 == len(sortList): # 끝번호에서,, 강의실 처리해줌
      if idx == False:
        if k == lecture_room: # 현재 강의실이 끝강의실인 경우
          lecture_room += 1 # 강의실 하나 더 추가~
          q.append((lecture_room, s, t))
        else: # 현재 강의실 말고 다른 강의실이 남았을 경우
          assign(k + 1) # 한번 더 서치..
      else : # True 일경우
        q.append((k, s, t)) # 동일한 강의실에 배정
      break

for i in range(N):
  s, t = map(int, sys.stdin.readline().rstrip().split())
  if i == 0 : # 처음이면 강의실 1 배정해준다.
    lecture_room += 1
    q.append((lecture_room, s, t))
  else: # 처음이 아니면
    assign(1) # 강의실 1부터 찾아본다.

print(lecture_room)