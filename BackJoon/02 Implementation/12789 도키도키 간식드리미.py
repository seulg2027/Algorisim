'''
12789번 도키도키 간식드리미
코드가 더럽지만,, 경우의 수를 잘 따져서 한번에 성공
 - 1~N까지의 수가 모두 있다는 것을 고려
'''

import sys
input = sys.stdin.readline

n = int(input())
now_waiting = list(map(int, input().split()))
other_space = []
done = False
num = 1

while True:
    if done == True or num == n+1: # 실패했거나, 모든 간식을 받았을 경우
        break
    
    if other_space: # 한 명씩만 설 수 있는 공간에 사람이 있을 경우
        if other_space[-1] == num:
            other_space.pop()
            num += 1
            continue
        elif now_waiting:
            if now_waiting[0] == num:
                now_waiting.pop(0)
                num += 1
                continue
            else:
                now = now_waiting.pop(0)
                other_space.append(now)
        else:
            done = True
    else: # 없을 경우
        now = now_waiting.pop(0)
        if now == num:
            num += 1
            continue
        else:
            other_space.append(now)
    #print(f" 11 {now_waiting} 22 {other_space}")

if not now_waiting and not other_space:
    print("Nice")
else:
    print("Sad")