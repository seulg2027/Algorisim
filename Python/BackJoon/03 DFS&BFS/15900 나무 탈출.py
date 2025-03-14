'''
15900 나무 탈출

DFS 코드 -> BFS로도 가능할 듯
'''

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = 0

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def order(now, move):
    global answer
    visited[now] = True
    is_leaf = 0
    
    for n in tree[now]:
        if not visited[n]:
            is_leaf += 1
            order(n, move+1)
    
    if is_leaf == 0:
        answer += move

order(1, 0)

# 홀수면 YES, 짝수이면 NO
print("Yes") if answer%2 != 0 else print("No")