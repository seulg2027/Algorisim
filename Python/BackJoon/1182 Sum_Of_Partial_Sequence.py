# 1182번 부분수열의 합

# # 내 풀이 1 백트래킹으로 시도 => 안됨...
# import sys
# input = sys.stdin.readline

# n, s = map(int, input().split())
# integers = list(map(int, input().split()))
# integers.sort()
# sum_of_num = 0
# sequence = [0] * (n+1)
# visited = [0] * (n+1)

# def make_sequence(x):
#   global n
#   if x == n+1:
#     for i in range(1, n+1):
#       print(sequence[i], end=' ')
#     print()
#   else:
#     for i in range(n):
#       # if max(sequence) < integers[i]:
#       visited[x] = 1
#       sequence[x] = integers[i]
#       make_sequence(x+1)
#       sequence[x] = 0
#       visited[x] = 0

# make_sequence(1)

# # 2. combinations를 사용하여 푼 코드

# import sys
# from itertools import combinations
# input = sys.stdin.readline

# n, s = map(int, input().split())
# integers = list(map(int, input().split()))
# cnt = 0

# for i in range(1, n+1):
#   comb = list(combinations(integers, i))
  
#   for j in comb:
#     sum_of_num = sum(j)
#     if sum_of_num == s:
#       cnt += 1

# print(cnt)


# 3. 백트래킹으로 다시 푼 코드

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
integers = list(map(int, input().split()))
cnt = 0

def make_sequence(idx, sub_sum):
  global cnt
  if idx >= n:
    return
  sub_sum += integers[idx]
  if sub_sum == s:
    print(integers[idx])
    cnt += 1
  make_sequence(idx+1, sub_sum) # 현재 idx를 선택한 경우의 가치
  make_sequence(idx+1, sub_sum - integers[idx]) # 현재 idx를 선택하지 않은 경우의 가치

make_sequence(0, 0)
print(cnt)