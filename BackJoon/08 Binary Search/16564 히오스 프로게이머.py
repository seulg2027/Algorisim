'''
16564번 히오스 프로게이머

레벨 : 10 15 20
차이 :   5  5

1. 이전 레벨과 차이를 계산, 현재까지의 레벨 개수만큼 격차를 올려주기
2. 만약 k가 부족하다면 k에서 현재까지의 레벨 개수를 나눠서 공평하게 레벨 올려주기, 끝!
   -> 최소 레벨 구하는 거라서 반올림 고려하지 말고 몫만 챙기기
'''

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
levels = []
for i in range(n):
    levels.append(int(input()))
levels.sort()

# 이전 레벨이랑 차이 계산해서 k에서 빼서 계산하기
for i in range(1, n):
    gap = levels[i] - levels[i-1]
    if gap * i <= k:
        k -= gap * i
        levels[:i+1] = list(levels[i] for _ in range((i+1)))
    else:
        plus = k // i
        print(levels[i-1] + plus)
        exit()

answer = min(levels)
if k > 0: # 만약 k가 남는다면
    plus = k // n
    answer = levels[0] + plus

print(answer)