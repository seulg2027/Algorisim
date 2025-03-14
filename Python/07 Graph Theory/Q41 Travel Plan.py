# Q41 여행 계획

# 내가 푼 방법
N, M = map(int, input().split())

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 부모 테이블 초기화
parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

graph = []

for _ in range(N):
  graph.append(list(map(int, input().split())))

# 그래프 확인하고 1인 곳만 루트노드 갱신해주기
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      union_parent(parent, i+1, j+1)

# 한울이가 갈 여행지 데이터 받기
trips = list(map(int, input().split()))
result = True
for i in range(M-1):
  if parent[trips[i]] != parent[trips[i+1]]:
    result = False

print("YES" if result == True else "False")