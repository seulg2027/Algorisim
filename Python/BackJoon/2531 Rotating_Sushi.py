# 2531번 회전 초밥

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = []
for _ in range(n):
  sushi.append(int(input()))
sushi.extend(sushi)

set_sushi = set()
set_sushi.update(sushi[0:k])
set_sushi.add(c)
max_value = len(set_sushi)

for i in range(k, n+k):
  set_sushi.add(sushi[i])
  if not sushi[i-k] in sushi[i-k+1:i+1] and sushi[i-k] != c:
    set_sushi.remove(sushi[i-k])
  max_value = max(max_value, len(set_sushi))

print(max_value)