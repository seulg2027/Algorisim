# 14889번 스타트와 링크

# 백트래킹 사용,, n=20 일 때 다른 output이 나오는 코드

# import sys
# input = sys.stdin.readline

# n = int(input())
# team_cnt = n//2
# s = [0] * (team_cnt+1)

# skills = [list(map(int, input().split())) for _ in range(n)]

# visited = [0] * team_cnt
# score = [0] * 3
# cnt = 0

# def plus_score(arr, x):
#   global cnt
#   if x == 3:
#     num = ''
#     for i in range(1, 3):
#       num += str(score[i])
#     cnt += skills[int(num[0])-1][int(num[1])-1]
#   else:
#     for j in range(0, team_cnt):
#       if not visited[j]:
#         visited[j] = 1
#         score[x] = arr[j]
#         plus_score(arr, x+1)
#         score[x] = 0
#         visited[j] = 0

# score_list = []

# def make_team(x):
#   global cnt
#   result = []
#   if x == team_cnt+1:
#     for i in range(1, team_cnt+1):
#       result.append(s[i])
#     cnt = 0
#     plus_score(result, 1)
#     score_list.append(cnt)
#   else:
#     for j in range(1, n+1):
#       if max(s) < j:
#         s[x] = j
#         make_team(x+1)
#         s[x] = 0

# make_team(1)
# min_value = sys.maxsize

# for i in range(len(score_list)//2):
#   min_value = min(min_value, abs(score_list[i] - score_list[len(score_list)-i-1]))

# print(min_value)

# 정답 코드 # 한 번 더 생각해보기

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
  global ans
  if cnt == n // 2:
    start, link = 0, 0
    for i in range(n): # 반복문 두 번 돌려야 모든 경우의 수를 구할 수 있음
      for j in range(n):
        if select[i] and select[j]:
          start += a[i][j]
        elif not select[i] and not select[j]:
          link += a[i][j]
    ans = min(ans, abs(start - link))
  
  # 백트래킹 코드 => 조합으로 팀짜기
  for i in range(idx, n):
    if select[i]:
      continue
    select[i] = 1
    dfs(i+1, cnt+1)
    select[i] = 0

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)