# 1713번 후보 추천하기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
good = list(map(int, input().split()))

photo_frame = []

for i in range(m):
  is_photo = False
  for photo in photo_frame: # 중복이 있는지 검사
    cdd, nb = photo
    if cdd == good[i]:
      idx = photo_frame.index(photo)
      photo_frame[idx] = (cdd, nb+1)
      is_photo = True # 중복 있음
      break
  if not is_photo: # 중복이 없을 경우
    if len(photo_frame) == n: # 사진틀이 꽉 찬 경우 가장 추천수가 낮은 학생 버림
      sortedframe = sorted(photo_frame, key=lambda x: x[1]) # 따로 담아줘야함..!
      photo_frame.remove(sortedframe[0])
      photo_frame.append((good[i], 1))
    else:
      photo_frame.append((good[i], 1))

photo_frame.sort()
for cdd, nb in photo_frame:
  print(cdd, end=' ')