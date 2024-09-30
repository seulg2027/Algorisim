'''
내림차순, 오름차순
맥주의 선호도 | 도수 레벨
4 3 = -1 #
3 3 = 0
1 4 = 3 #
2 5 = 3
4 6 = 2

-- 두번째, 다른 사람 풀이 참고
오름차순, 오름차순
3 3 #
4 3
1 4 #
2 5 #
4 6
'''

import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
drinks = list(list(map(int, input().split())) for _ in range(k))

drinks.sort(key=lambda x : (x[1], x[0]))
q = []
prefer = 0
answer = -1

# 맥주 하나씩 검사
for beer in drinks:
    prefer += beer[0]
    heapq.heappush(q, beer[0]) # 선호도만 넣으면 됨. 도수 레벨은 넣을 필요 없음
    
    if len(q) == n:
        if prefer >= m:
            answer = beer[1]
            break
        else:
            prefer -= heapq.heappop(q)

print(answer)