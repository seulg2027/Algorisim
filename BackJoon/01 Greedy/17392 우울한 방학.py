'''
17392번 우울한 방학

최대한 약속을 일정한 간격으로 잡는 것이 유리 -> 우울함이 마이너스이면 제곱으로 불어나기 때문
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
appointments = list(map(int, input().split()))

mood_day = sum(appointments) + n # 기분이 모두 0 이상으로 유지될 수 있는 최대 날짜 수

# 우울함을 느끼지 않을 최대 날짜수가 주어진 방학 일수보다 많으면
if mood_day >= m:
    print(0)
    exit(0)
# 아니라면 우울함 계산
else:
    arr = [0 for _ in range(n+1)] # 기분(마이너스) 수치 / n+1은 약속 앞, 뒤로 비는 공간의 개수
    ans = [0 for _ in range(n+1)] # 우울함 계산
    x = m - mood_day # 우울함을 느끼는 날짜 수
    now = 0
    while x > 0:
        if now == n+1:
            now = 0
        arr[now] += 1
        ans[now] += arr[now] * arr[now] # 기분에 맞춰 우울함은 제곱이 됨
        x -= 1
        now += 1

print(sum(ans))