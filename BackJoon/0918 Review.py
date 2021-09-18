## 주유소 ##


n = int(input())
km = list(map(int, input().split()))
gas = list(map(int, input().split()))
mp = gas[0]
res = 0

for i in range(n-1):
  if gas[i] < mp:
    mp = gas[i]
  res += km[i]*mp
print(res)


## 우주 탐사선 ##


# 플로이드 + DFS
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n , start = map(int,input().split())
visited = [False] *(n)
visited[start] = True
answer = int(1e9) 

def dfs(position,visit_count,cost):
    global answer
    
    if visit_count == n:
        answer = min(answer,cost)
        return 
        
    for i in range(n):
        if visited[i] == False: # 아직 방문하지 않았다면,
            visited[i] = True # 방문처리해주고
            dfs(i,visit_count+1,cost+graph[position][i]) # dfs(현재,visit카운트,비용)
            visited[i] = False # 다시 미방문처리

graph = [list(map(int,input().split())) for _ in range(n)]
# i행성에서 j행성까지 가는 최단거리 구하기(플로이드)
# 여기서 이미 방문한 행성도 중복해서 갈 수 있다고 했다.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])

# 이제 행성을 탐색하면서 최단 경로를 구하면 된다.

dfs(start,1,0)
print(answer)