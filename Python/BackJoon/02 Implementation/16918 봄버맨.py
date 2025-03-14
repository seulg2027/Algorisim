'''
16918 봄버맨
DFS인줄 알았는데 구현이었다.. 속았엉..😵‍💫
최대한 for 문 안쓰도록 하려고 노력했는데 3중 반복문을 써버렸다^^... 그래도 input 값이 많이 안커서 다행

1 ≤ R, C, N ≤ 200
'''

import sys, copy

input = sys.stdin.readline

R, C, N = map(int, input().split())
cross_table = [input().rstrip() for _ in range(R)]
seconds_table = list() # 폭탄 설치 후 몇 초가 지났는지 표시한 테이블

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 1
for i in range(R):
    seconds_table.append(list(cross_table[i].replace('O', '1'))) # 2번까지 수행

def plus_second():
    for i in range(R):
        for j in range(C):
            if seconds_table[i][j] == '.': # 폭탄 설치
                seconds_table[i][j] = 0
            elif seconds_table[i][j] == '1': # 예외 처리
                seconds_table[i][j] = 2
            else:
                seconds_table[i][j] += 1

def bumb():
    for i in range(R):
        for j in range(C):
            if cross_table[i][j] == 3:
                seconds_table[i][j] = '.' # 폭탄 터짐
                for n in range(4):
                    rx = i + dx[n]
                    ry = j + dy[n]
                    if 0 <= rx < R and 0 <= ry < C:
                        seconds_table[rx][ry] = '.' # 폭탄 터짐

while cnt < N:
    if cnt == N:
        break
    
    if cnt % 2 != 0:
        # 3번 (1초 지난 뒤 폭탄 설치)
        cnt += 1
        plus_second()
    else:
        # 4번 (1초 지난 뒤 폭탄 터짐)
        cnt += 1
        plus_second() # 폭탄 설치 하는 경우의 수는 없음. seconds를 추가할 뿐
        cross_table = copy.deepcopy(seconds_table)
        bumb()

for a in range(R):
    for b in range(C):
        if seconds_table[a][b] == '.':
            print('.', end='')
        else:
            print('O', end='')
    print()
