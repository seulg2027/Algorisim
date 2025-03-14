# 10025 게으른 백곰

# 투포인터

import sys, copy
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [0 for _ in range(1000001)]
max_value = 0

for _ in range(n):
  g, x = map(int, input().split())
  graph[x] = g
  max_value = max(x, max_value)

left = 0
right = left + k * 2
ans = sum(graph[left:right+1])
value = sum(graph[left:right+1])

while right <= max_value:
  right += 1
  value += graph[right]
  value -= graph[left]
  if value > ans:
    ans = copy.copy(value)
  left += 1

print(ans)