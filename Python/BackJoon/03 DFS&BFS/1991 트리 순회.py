'''
1991번 트리 순회

DFS 개념
'''

import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().strip().split()
    tree[root] = (left, right)

## 전위 순회
## 트리 -> 왼쪽 노드 -> 오른쪽 노드
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

## 중위 순회
## 왼쪽 노드 -> 트리 -> 오른쪽 노드
def midorder(root):
    if root != '.':
        midorder(tree[root][0])
        print(root, end='')
        midorder(tree[root][1])

## 후위 순회
## 왼쪽 노드 -> 오른쪽 노드 -> 트리
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
midorder('A')
print()
postorder('A')