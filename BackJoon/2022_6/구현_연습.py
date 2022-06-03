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


# 1614번 영식이의 손가락

# 처음엔 dp인줄 알았지만 손가락이 5개밖에없어서 하나하나 다 계산

import sys
input = sys.stdin.readline

n = int(input())
cnt = int(input())

first = n-1
if n == 1 or n == 5:
  ans = first + 8*cnt
else: # n이 2,3,4
  t = cnt // 2
  r = cnt % 2
  if n == 2:
    ans = first + 8*t + 6*r
  elif n == 3:
    ans = first + 8*t + 4*r
  else:
    ans = first + 8*t + 2*r

print(ans)