'''
12933번 오리

'''

import sys
input = sys.stdin.readline

record = input().rstrip()
n = len(record)
visited = [False for _ in range(n)]
duck = "quack"

ans = 0
cnt = 0

# 첫문자열은 q, 끝문자열은 k 이고 5로 나누어지는 문자열이어야 함
if record[0] != 'q' or n % 5 != 0 or record[-1] != 'k':
    print(-1)
    exit(0)

while True:
    # 모든 오리를 방문했을 때
    if False not in visited:
        break
    # 이미 n-4번 돌았을 때
    if cnt == n-4:
        ans = -1
        break
    
    is_True = False
    cnt += 1
    now = 0
    for i in range(n):
        if not visited[i] and record[i] == duck[now]:
            visited[i] = True
            now += 1
            if record[i] == "k":
                now = 0
                is_True = True
    
    if is_True: ans += 1

print(ans)