# 06-1 팀 결성

N, M = map(int, input().split())

# 부모 찾는 함수 ( 같은 집합인지 확인하는 합수 )
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a # 부모 집합 바꿔주기
  else:
    parent[a] = b

# 부모 테이블 초기화
parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

for _ in range(M):
  is_team, a, b = map(int, input().split())
  # 팀 합치기 연산
  if is_team == 0:
    union(parent, a, b)
  # 같은 팀 여부 확인 연산
  elif is_team == 1:
    a_team = find_parent(parent, a)
    b_team = find_parent(parent, b)
    if a_team == b_team:
      print("YES")
    else:
      print("NO")