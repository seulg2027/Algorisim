'''
2260번 회장뽑기
진짜 기본적인 BFS 그래프 문제
'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
friends = [[] for _ in range(n+1)] # 친구 그래프
answer = []

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friends[a].append(b)
    friends[b].append(a) # 양방향이므로 둘 다 넣어주기

def bfs(x):
    visited = [False for _ in range(n+1)] # 방문 여부
    q = deque([(x, 0)])
    visited[x] = True
    while q:
        now = q.popleft()
        for i in friends[now[0]]:
            if not visited[i]:
                q.append([i, now[1]+1])
                visited[i] = True
        cnt = now[1]
    return cnt

score = sys.maxsize
for j in range(1, n+1):
    cnt = bfs(j)
    if score > cnt:
        score = cnt
    answer.append(cnt)

people = answer.count(score)
print(f"{score} {people}")
for sc in range(n):
    if answer[sc] == score:
        sc += 1
        print(f"{sc}", end=" ")