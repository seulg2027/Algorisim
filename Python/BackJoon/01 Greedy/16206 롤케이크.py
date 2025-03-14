'''
16206번 롤케이크

경우의 수를 잘 생각해야하는 그리디 문제
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort()

## x에는 10으로 나누어지는 케익 넣기, y에는 10으로 나누어지지 않는 케이크 넣기
## 10으로 나누어지는 케익이 더 우선순위가 높기 때문
cakes_x = []
cakes_y = []
for c in cakes:
    if c % 10 != 0:
        cakes_y.append(c)
    else:
        cakes_x.append(c)
cnt = 0
cakes = cakes_x + cakes_y

for cake in cakes:
    if M == 0:
        break
    
    if cake == 10:
        cnt += 1
    elif cake > 10:
        tmp = cake
        # 10씩 케이크 자르기
        while tmp // 10 > 0:
            if tmp == 10:
                cnt += 1
                break
            if M == 0:
                break
            M -= 1
            cnt += 1
            tmp -= 10

print(cnt)