'''
1193 분수찾기
'''

import sys
input = sys.stdin.readline

X = int(input())
cnt = 1
cycle = 1

while True:
    if X <= cycle:
        if cnt % 2 == 0: # 주기가 짝수일 경우
            numer = X - (cycle - cnt) # 분자
            deno = cnt+1 - X + (cycle - cnt) # 분모
        else:
            numer = cnt+1 - X + (cycle - cnt) # 분자
            deno = X - (cycle - cnt)
        break
    
    cnt += 1
    cycle += cnt

print(f"{numer}/{deno}")