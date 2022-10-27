'''
86971 전력망을 둘로 나누기

최소 신장 트리에서 주의할 점 : 부모 배열의 경로 압축⭐️⭐️⭐️
간선이 순서대로 주어지지 않을 경우 바로 이전 부모 노드로 나오기 때문에 주의할 것.
'''

from collections import Counter

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

def solution(n, wires):
    answer = int(1e9)
    
    for i in range(n-1): # i번째 wire가 없을 경우
        parent = [i for i in range(n+1)]
        
        for j in range(n-1):
            a, b = wires[j]
            if i == j or find_parent(parent, a) == find_parent(parent, b):
                continue
            union_parent(parent, a, b)
        
        value = []
        for i in range(1, n+1):
            value.append(find_parent(parent, i)) # 간선을 따로 만들어주어야 함
        
        value = Counter(value) # parent값을 Counter로 세기. Counter 라이브러리 알고 있으면 편함
        v = list(value.values()) 
        answer = min(answer, abs(v[0] - v[1]))
        
    return answer
