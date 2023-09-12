'''
거리두기 확인하기
'''

from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(graph, x, y):
    q = deque([(x, y, 0)]) # 대기실 위치 x, y, 맨해튼거리
    while q:
        a, b, dist = q.popleft()
        #print(f"x={x} y={y} a={a} b={b} dist={dist}")
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            manheton = dist + abs(dx[i]) + abs(dy[i])
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx != x or ny != y): # 처음 위치랑 같으면 안돼
                if manheton <= 2: # "X" 인 경우를 만나면 맨해튼 신경 안써도 좋아
                    if graph[nx][ny] == "O": # "O"를 만나면 큐 append
                        q.append((nx, ny, manheton))
                    if graph[nx][ny] == "P": # "P"를 만나면 맨해튼 거리 2보다 이하면 탈락
                        if manheton <= 2:
                            return False
    return True
            

def solution(places):
    answer = []
    
    for c in range(5):
        result = True
        place_ans = []
        for i in range(5):
            for j in range(5):
                if places[c][i][j] == 'P': # 지원자일 경우
                    result = bfs(places[c], i, j)
                    place_ans.append(result)
        
        if False in place_ans: # 거리두기 실패
            answer.append(0)
        else: # 성공
            answer.append(1)
    
    return answer