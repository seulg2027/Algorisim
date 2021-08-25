# Q43 어두운 길

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

# 부모 노드
parent = [0] * N # 0번 ~ N-1번
for i in range(N):
  parent[i] = i # 부모노드 초기화~

# 간선을 담을 리스트
edges = []

for i in range(M):
  x, y, z = map(int, input().split())
  edges.append((z, x, y))

# 비용 순으로 정렬
edges.sort()
# 비용을 더할 변수
result = 0

# 비용을 돌아봄
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b): # 만약 아직 집합연산이 안 일어났다면
    union_parent(parent, a, b) # 집합 실행
    result += cost # 비용 추가

print(result)