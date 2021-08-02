## 연구소 생각해봐야할 답


from collections import deque
import copy

n, m = map(int, input().split())
test = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 2]
]

lab = test
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0


def bfs(lab):
    graph = copy.deepcopy(lab)
    global answer
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append([i, j])
    print(queue)
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = dx+x, dy+y            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append([nx, ny])
    print(1)
    
    cnt = 0
    for i in graph:
        cnt += i.count(0)
        print(cnt)
    answer = max(cnt, answer)
    return answer


def laboratory(cnt):
    if cnt == 3:
        global answer
        answer = bfs(lab)
        return 
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                laboratory(cnt+1)
                lab[i][j] = 0

answer = 0
queue = deque([])
print(laboratory(0))

print(answer)