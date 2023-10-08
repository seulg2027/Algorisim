"""
1620번 나는야 포켓몬 마스터 이다솜
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pocketmons = [input().strip() for _ in range(n)]

for i in range(m):
    quest = input().strip()
    if quest.isdigit():  # 숫자인지 판별해주는 함수 isdigit()
        quest = int(quest)
        print(pocketmons[quest - 1])
    else:
        print(pocketmons.index(quest) + 1)
