# 국영수

# n = int(input())
# students = []

# for _ in range(n):
#   student, k, e, m = map(str, input().split())
#   students.append([student, int(k), int(e), int(m)])

# sorted_students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# for i in range(n):
#   print(sorted_students[i][0]) 

# 먹을 것인가 먹힐 것인가

# import sys

# time = int(sys.stdin.readline())
# result = [0] * time

# for idx in range(time):
#   a, b = map(int, sys.stdin.readline().split())
#   a_list = list(map(int, sys.stdin.readline().split()))
#   b_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
#   for i in range(a):
#     j = 0
#     while j < b:
#       if b_list[j] < a_list[i]:
#         result[idx] += (b - j)
#         break
#       j += 1

# for re in result:
#   print(re) 

# # 올림픽

# import sys

# n, k = map(int, sys.stdin.readline().split())
# data = []
# ranks = [1e9] * n

# for i in range(n):
#   glo, gold, sliver, bronze = map(int, sys.stdin.readline().split())
#   data.append([glo, gold, sliver, bronze])
# sorted_medal = sorted(data, key=lambda x:(-x[1], -x[2], -x[3]))

# rank = 0

# for j in range(n):
#   if k == j:
#     print(ranks[k-1])
#     break
#   start = sorted_medal[j]
#   end = sorted_medal[j+1]
#   if start[1] == end[1] and start[2] == end[2] and start[3] == end[3]:
#     rank += 1
#     ranks[j] = min(rank, ranks[j])
#     ranks[j+1] = ranks[j]
#   else:
#     rank += 1
#     ranks[j] = min(rank, ranks[j])

# 1431 시리얼 번호
import sys
data = []

for i in range(int(sys.stdin.readline().rstrip())):
  st = sys.stdin.readline().rstrip()
  cnt = 0
  for j in st:
    try:
      cnt += int(j)
    except:
      continue
  data.append((st, cnt))

data = sorted(data, key=lambda x: (len(x[0]), x[1], x[0]))

for item in data:
  print(item[0])