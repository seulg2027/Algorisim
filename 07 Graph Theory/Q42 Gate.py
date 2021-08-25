# Q42 탑승구

G = int(input())
P = int(input())

def find_parent(parent, a):
  if a <= parent[a]:
    parent[a] = find_parent(parent, a)
  return parent[a]

parent = [[] for _ in range(P+1)]

for i in range(1, P+1):
  gate = int(input())
  parent.append(i, )