'''
1912번 연속 합
'''

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
m = list(0 for _ in range(n))
m[0] = seq[0]

for i in range(1, n):
    m[i] = max(seq[i], seq[i]+m[i-1])

print(max(m))