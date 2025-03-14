# 더 맵게

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

h = []

def solution(scoville, K):
  answer = 0
  for item in scoville:
    heapq.heappush(h, item)
  while h:
    now = heapq.heappop(h)
    if now < K:
      if not h: # 힙이 비었다면
        return -1
      next = heapq.heappop(h)
      new = now + next * 2
      heapq.heappush(h, new)
      answer += 1
    else:
      return answer

print(solution(scoville, K))