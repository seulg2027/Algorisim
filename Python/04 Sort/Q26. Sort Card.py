# Q26 카드 정렬하기

# 내가 푼 방법
# 백준에서는 메모리 초과... 라이브러리 때문에 그런가ㅠ
import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
cards = []
for i in range(n):
  cards.append(int(input()))

nPr = list(permutations(cards, n)) # 순열 만들기
compare = 0
result = 0
answer = [] # 순열에 대해 카드를 정렬한 횟수를 리스트 만들어서 넣기

for card in nPr:
  compare = card[0] + card[1] # 초깃값 설정
  result = compare
  for i in range(2, n): # 세번째 카드서부터 규칙적으로 더하기
    compare += card[i]
    result += compare # result에 따로 더해주어야 결과적으로 compare가 두번 더해짐
  answer.append(result)

print(min(answer))


###################################   답안 예시    ###################################

import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입한다.
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)

result = 0
while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음을 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # 카드 묶음을 합쳐서 다시 삽입
  sum_value = one + two
  # 합친 카드를 result에 더함
  result += sum_value
  heapq.heappush(heap, sum_value)

print(result)