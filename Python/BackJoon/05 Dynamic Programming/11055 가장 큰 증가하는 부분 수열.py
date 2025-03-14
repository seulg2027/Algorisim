'''
11055번 가장 큰 증가하는 부분 수열

n이 1,000 이라서 가능했던 풀이
'''

import sys, copy
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = copy.deepcopy(A)

# 1000 * 999
for i in range(n):
    max_value = 0
    for j in range(i):
        if A[i] > A[j]:
            max_value = max(max_value, dp[j])
    dp[i] += max_value

print(max(dp))