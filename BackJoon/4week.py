# # 기타 레슨

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# lessons = list(map(int, input().split()))

# minlesson = max(lessons)
# sumlesson = sum(lessons)
# ans = int(1e9)

# while minlesson <= sumlesson:
#   mid = (minlesson + sumlesson) // 2
#   cnt = 0
#   sum_num = 0
#   for i in range(len(lessons)):
#     if sum_num + lessons[i] > mid:
#       cnt += 1
#       sum_num = 0
#     sum_num += lessons[i]
#   if sum_num:
#     cnt += 1
  
#   if cnt > m:
#     minlesson = mid + 1
#   else:
#     ans = min(ans, mid)
#     sumlesson = mid - 1

# print(ans)

# 게임 

X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
  print(-1)
else:
  answer = 0
  left = 1
  right = X
  
  while left <= right:
    mid = (left + right) // 2
    if ((Y + mid) * 100 // (X + mid)) <= Z:
      left = mid+1
    else:
      answer = mid
      right = mid - 1
  
  print(answer)