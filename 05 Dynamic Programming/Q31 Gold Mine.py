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


###################################   답안 예시    ###################################
for tc in range(int(input())):
  n, m = map(int, input().split())
  array = list(map(int, input().split()))

  dp = []
  index = 0
  # dp테이블에 추가해줌
  for i in range(n):
    dp.append(array[index: index+m])
    index += m

  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0:
        left_up = 0
      else:
        left_up = dp[i-1][j-1]
      # 왼쪽 아래에서 오는 경우
      if i == n-1:
        left_down = 0
      else:
        left_down = dp[i+1][j-1]
      left = dp[i][j-1]
      dp[i][j] += max(left_up, left_down, left)
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  
  print(result)