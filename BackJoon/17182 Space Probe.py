# 우주 탐사선


# 플로이드 알고리즘 -> 크루스칼 -> 다시 플로이드..

INF = int(1e9)

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 발사되는 위치에서 false, 발사되지 않는 위치에서 true(방문하였다는 표시)
not_visited = [False if i == k else True for i in range(n)]

minval = [INF]

def DFS(r, c, time, depth):
    if depth == n-1: # 깊이가 n-1일 경우,, 그러니까 모든 행성을 방문했을 경우
        minval[0] = min(minval[0], time) # 최솟값 갱신해줌
        return

    if time > minval[0] : # 예외 처리
        return

    for j in range(n):
        if j != c and not_visited[j]:
            not_visited[j] = False
            DFS(c, j, time + arr[c][j], depth+1) # 행성 방문횟수 늘여서 재귀호출해줌
            not_visited[j] = True

for tt in range(n):
    for i in range(n):
        for j in range(n):
            if i == j : continue
            arr[i][j] = min(arr[i][j], arr[i][tt] + arr[tt][j]) # 최솟값 갱신해주기

for c in range(n):
    if k != c and not_visited[c]: # 발사되는 위치 제외하고 모든 위치에서 방문 표시 해주기
        not_visited[c] = False # 발사되었다...
        DFS(k, c, arr[k][c], 1) # 발사되는 위치 제외
        not_visited[c] = True # 다시 방문 표시 초기화

print(minval[0])