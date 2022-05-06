# 2559번 수열

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
degrees = list(map(int, input().split()))

right = k - 1
degree = sum(degrees[:right+1])
ans = [degree]

for left in range(n-k):
  degree -= degrees[left]
  right += 1
  degree += degrees[right]
  ans.append(degree)

print(max(ans))