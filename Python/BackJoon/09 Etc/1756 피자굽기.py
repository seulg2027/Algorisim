'''
1756번 피자굽기

오븐 지름 : 5 6 4 3 6 2 3
피자 반죽 :   5   2 3
↓ 앞보다 작은 지름 선택
오븐 지름 : 5 5 4 3 3 2 2
피자 반죽 :   5   2 3

(처음 생각) : 시간초과
1. 딕셔너리 만들기
2. 작은 수 찾기 -> 작은 수 배열에서 가장 작은 인덱스를 가지고 있는 것
---
(다시 시도한 생각)
1. 지름을 앞에 있는 지름과 비교해 작은 지름으로 선택하기! 어차피 앞에 더 작은 지름이 있으면 피자가 안넣어지기 때문
2. 뒤부터 피자를 넣기, position을 활용해 피자를 넣을지 말지 선택
'''

import sys
input = sys.stdin.readline

d, n = map(int, input().split())
oven_radius = list(map(int, input().split()))
pizza_radius = list(map(int, input().split()))

for i in range(1, d):
    oven_radius[i] = min(oven_radius[i], oven_radius[i-1])

position = d
for pizza in pizza_radius:
    while position > 0 and oven_radius[position-1] < pizza:
        position -= 1
    
    if position == 0:
        print(0)
        exit(0)
    
    position -= 1

print(position + 1)