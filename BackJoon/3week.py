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
# input = sys.stdin.readline
# n, k = map(int, input().split())
# s = []
# for i in range(n):
#   s.append(list(map(int, input().split())))
# s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
# for i in range(n):
#   if s[i][0] == k:
#     index = i
# for i in range(n):
#   if s[index][1:] == s[i][1:]:
#     print(i + 1)
#     break

# # 1431 시리얼 번호
# import sys
# data = []

# for i in range(int(sys.stdin.readline().rstrip())):
#   st = sys.stdin.readline().rstrip()
#   cnt = 0
#   for j in st:
#     try:
#       cnt += int(j)
#     except:
#       continue
#   data.append((st, cnt))

# data = sorted(data, key=lambda x: (len(x[0]), x[1], x[0]))

# for item in data:
#   print(item[0])

# # 10814 나이순 정렬
# n = int(input())
# data = []

# for i in range(n):
#   age, mem = map(str, input().split())
#   data.append((int(age), mem))

# data = sorted(data, key=lambda x: x[0])

# for j in range(n):
#   print(data[j][0], data[j][1])

# # 2910 빈도 정렬
# import sys

# n, c = map(int, sys.stdin.readline().split())
# data = list(map(int, sys.stdin.readline().split()))

# dic = dict()

# for idx in data:
#   if idx not in dic:
#     dic[idx] = 0
#   dic[idx] += 1

# dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

# for x, y in dic:
#   for _ in range(y):
#     print(x, end=' ')

# # 11399 ATM
# import sys

# n = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# data.sort()
# cal = [0] * n

# for idx in range(n):
#   for j in data[:idx+1]:
#     cal[idx] += j

# result = 0
# for item in cal:
#   result += item

# print(result)