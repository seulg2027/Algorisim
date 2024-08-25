'''
15903번 카드 합체 놀이
'''

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards) # heap 모두 넣기

while True:
    if m == 0:
        break
    
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    
    for _ in range(2):
        heapq.heappush(cards, card1+card2)
    
    m -= 1

print(sum(cards))
