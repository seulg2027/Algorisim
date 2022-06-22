# 1946번 신입 사원

# 힌트보고 품,,

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  emps = []
  for _ in range(n):
    a, b = map(int, input().split())
    emps.append([a, b])
  
  emps.sort(key=lambda x: x[0]) # 사원을 서류 순위로 정렬
  ans = 1
  max_value = emps[0][1] # 1번 사원의 면접 순위
  
  # 사원의 면접 순위보다 높을 때만
  for i in range(1, n):
    if max_value > emps[i][1]:
      ans += 1
      max_value = emps[i][1]
  print(ans)
