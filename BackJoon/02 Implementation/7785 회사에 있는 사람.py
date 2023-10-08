"""
7785번 회사에 있는 사람
* 집합 "제거" 추가
"""

import sys

input = sys.stdin.readline

people = set()

for _ in range(int(input())):
    person, log = input().split()
    if log == "enter":
        people.add(person)
    elif log == "leave":
        people.remove(person)

people = sorted(list(people), reverse=True)

for p in people:
    print(p)
