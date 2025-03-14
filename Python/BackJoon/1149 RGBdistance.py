# RGB 거리


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def dynamic_cal():
  for i in range(1, n):
    graph[i][0] = graph[i][0]+min(graph[i-1][1], graph[i-1][2])
    graph[i][1] = graph[i][1]+min(graph[i-1][0], graph[i-1][2])
    graph[i][2] = graph[i][2]+min(graph[i-1][0], graph[i-1][1])

dynamic_cal()

print(min(graph[n-1]))
