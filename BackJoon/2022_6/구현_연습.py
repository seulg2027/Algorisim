# # 23814번 아 저는 볶음밥이요

# # 볶음밥 먹고 싶다
# # 첫번째 시도 후 다시,,, 생각

# import sys
# input = sys.stdin.readline

# d = int(input())
# n, m, k = map(int, input().split())

# dumpling = (n+m+k)//d
# remain = (n+m+k)%d

# # 조건이 맞을 때까지 옮기는 작업을 반복해줘야함..!
# while (n//d) + (m//d) + (k//d) != dumpling:
#   n_value = n % d
#   m_value = m % d
  
#   if n_value > m_value:
#     n += (d-n_value)
#     k -= (d-n_value)
#   elif n_value < m_value:
#     m += (d-m_value)
#     k -= (d-m_value)
#   else:
#     n += (d-n_value)
#     m += (d-m_value)
#     k -= (d-n_value) + (d-m_value)
# print(k)


# # 1614번 영식이의 손가락

# # 처음엔 dp인줄 알았지만 손가락이 5개밖에없어서 하나하나 다 계산

# import sys
# input = sys.stdin.readline

# n = int(input())
# cnt = int(input())

# first = n-1
# if n == 1 or n == 5:
#   ans = first + 8*cnt
# else: # n이 2,3,4
#   t = cnt // 2
#   r = cnt % 2
#   if n == 2:
#     ans = first + 8*t + 6*r
#   elif n == 3:
#     ans = first + 8*t + 4*r
#   else:
#     ans = first + 8*t + 2*r

# print(ans)


# # 2659번 십자카드 문제

# # 문제를 잘못 이해해서 한참을 헤맴..
# # 시계수를 하나하나 검사해줘야했음

# import sys
# input = sys.stdin.readline

# card = list(input().split())

# def is_clock(card):
#   card += card
#   clock_num = int("".join(card[0:4]))
#   for i in range(1, 4):
#     item = "".join(card[i:i+4])
#     clock_num = min(int(item), clock_num) # 시계수 구하기
#   return clock_num

# clock_num = is_clock(card)

# cnt = 0
# for num in range(1111, clock_num):
#   l = list(str(num))
#   if '0' in l:
#     continue
#   if num == is_clock(l):
#     cnt += 1

# print(cnt+1)


# 2503 숫자 야구

import sys
import numpy
input = sys.stdin.readline

n = int(input())
candidate = [1 for _ in range(110, 1000)]

# 111 부터 999까지 수들 중 안되는 수를 제외
for i in range(110, 1000):
  if '0' in list(str(i)):
    candidate[i-110]= 0

c = numpy.array(candidate)

for _ in range(n):
  number, a, b = map(int, input().split())
  candidate[number] = 0
  
  # 스트라이크
  if a > 0:
    list_num = list(str(number))
    for m in range(110, 1000):
      if candidate[m-110]:
        cnt_a = 0
        list_m = list(str(m))
        for j in range(3):
          if list_num[j] == list_m[j]:
            cnt_a += 1
        if cnt_a < a:
          candidate[m-110] = 0
  
  # 볼
  if b > 0:
    set_num = set(list(str(number)))
    for m in range(110, 1000):
      if candidate[m-110]:
        set_m = set(list(str(m)))
        re = set_num - set_m
        if 3-len(re) < b:
          candidate[m-110] = 0
    
    # 볼이 있는데 스트라이크가 0
    if a == 0:
      list_num = list(str(number))
      for m in range(110, 1000):
        if candidate[m-110]:
          list_m = list(str(m))
          for j in range(3):
            if list_num[j] == list_m[j]:
              candidate[m-110] = 0
              break


print(numpy.where(c==1))