# 12927번 배수 스위치

import sys
input = sys.stdin.readline

bulbs = list(input().rstrip())
cnt = 0
lights = []

while True:
  if 'Y' not in bulbs: # 만약 Y가 더이상 없으면 => 정답 출력
    print(cnt)
    break
  yes = bulbs.index('Y') # Y가 있다면 index를 구해서
  if (yes+1) in lights: # 이미 앞에서 계산한 index라면.. 실 패
    print(-1)
    break
  lights.append(yes+1)
  for i in range(len(bulbs)):
    if (i+1) % (yes+1) == 0:
      bulbs[i] = 'N' if bulbs[i] == 'Y' else 'Y'
  cnt += 1