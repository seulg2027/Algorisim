# Q31 금광

T = int(input())

for t in range(T):
  n, m = map(int, input().split())
  data = list(map(int, input().split()))
  # 테이블 초기화
  dp = [0] * n
  array = []
  index = 0

  for i in range(n):
    array.append(data[index: index +m])
    index += m
  
  for i in range(n):
    now = i # 현재 금광의 위치
    for j in range(m):
      if (now-1) >= 0 and (now+1) < n:
        result = max(array[now-1][j], array[now][j], array[now+1][j])
        dp[i] += result
        if result == array[now-1][j]:
          now - 1
        if result == array[now+1][j]:
          now + 1
      elif (now-1) < 0 and (now+1) < n:
        result = max(array[now][j], array[now+1][j])
        dp[i] += result
        if result == array[now+1][j]:
          now + 1
      elif (now-1) >= 0 and (now+1) >= n:
        result = max(array[now-1][j], array[now][j])
        dp[i] += result
        if result == array[now-1][j]:
          now - 1
    print(dp[i])