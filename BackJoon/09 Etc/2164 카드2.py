'''
카드2
너무 간단..
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range(1, n+1)])
last_card = 0

while cards:
    trash_card = cards.popleft()
    
    try:
        return_card = cards.popleft() # 그 다음 카드가 있을 경우
        cards.append(return_card)
    except:
        last_card = trash_card # 그 다음 카드가 없으면
        break

print(last_card)