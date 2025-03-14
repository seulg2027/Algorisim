'''
7682번 틱택토

'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, nx, ny):
    q = deque([(x, y, graph[x][y])])
    while q:
        now = q.popleft()
        if (now[0] == 2 and nx == 1) or (now[1] == 2 and ny == 1) or (now[0] == 2 and now[1] == 2):
            return 1
        if 0 <= now[0]+nx < 3 and 0 <= now[1]+ny < 3:
            if graph[now[0]+nx][now[1]+ny] == now[2]:
                q.append((now[0]+nx, now[1]+ny, graph[now[0]+nx][now[1]+ny]))
    return 0

while True:
    game = input().rstrip()
    if game == "end":
        break
    
    graph = []
    for i in range(3):
        inner = [game[x] for x in range(9) if i*3+2 >= x >= i*3]
        graph.append(inner)
    
    # 말의 개수 체크
    x_cnt = game.count('X')
    o_cnt = game.count('O')
    if x_cnt-o_cnt not in [0, 1] or x_cnt > 5 or o_cnt > 4:
        print("invalid")
        continue
    
    is_full = 0
    bingo = [0, 0]
    for i in range(3):
        for j in range(3):
            ans = 0
            if graph[i][j] == '.': # 말이 다 차지 않은 채 종료
                is_full = 1
            
            if j == 0:
                ans += bfs(i, j, 0, 1)
            if i == 0:
                ans += bfs(i, j, 1, 0)
            if i == 0 and j == 0:
                ans += bfs(i, j, 1, 1)
            if i == 2 and j == 0:
                ans += bfs(i, j, -1, 1)
            
            if graph[i][j] == 'X':
                bingo[0] += ans
            elif graph[i][j] == 'O':
                bingo[1] += ans
    
    # 승자가 둘이다, 게임판이 다 안찼는데 승자가 존재하지 않는다.
    if (is_full == 1 and 1 not in bingo) or (bingo[0]>=1 and bingo[1]>=1):
        print("invalid")
        continue
    
    # 이것때메 한참 헤맴.. 여러 개 빙고가 나와도 오케이ㅠㅠ
    if bingo[0] in (1, 2) and x_cnt-o_cnt == 1:
        print("valid")
    elif bingo[1] == 1 and x_cnt-o_cnt == 0:
        print("valid")
    elif bingo[0] == 0 and bingo[1] == 0 and is_full == 0:
        print("valid")
    else:
        print("invalid")

