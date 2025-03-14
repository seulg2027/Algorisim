'''
15787 기차가 어둠을 헤치고 은하수를

구현
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = list([0]*20 for _ in range(n))
answer = []

for _ in range(m):
    order = list(map(int, input().split()))
    if order[0] == 1:
        train[order[1]-1][order[2]-1] = 1
    elif order[0] == 2:
        train[order[1]-1][order[2]-1] = 0
    elif order[0] == 3:
        train[order[1]-1].insert(0, 0)
        train[order[1]-1].pop()
    elif order[0] == 4:
        train[order[1]-1].append(0)
        train[order[1]-1].pop(0)

for j in range(n):
    if train[j] not in answer:
        answer.append(train[j])

print(len(answer))
