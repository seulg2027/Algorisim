# 23814번 아 저는 볶음밥이요

# 볶음밥 먹고 싶다
# 첫번째 시도 후 다시,,, 생각

import sys
input = sys.stdin.readline

d = int(input())
n, m, k = map(int, input().split())

dumpling = (n+m+k)//d
remain = (n+m+k)%d

if (n//d) + (m//d) + (k//d) == dumpling:
  print(k)
else:
  # 조건이 맞을 때까지 옮기는 작업을 반복해줘야함..!
  while (n//d) + (m//d) + (k//d) != dumpling:
    n_value = n % d
    m_value = m % d
    
    if n_value > m_value:
      n += (d-n_value)
      k -= (d-n_value)
    elif n_value < m_value:
      m += (d-m_value)
      k -= (d-m_value)
    else:
      n += (d-n_value)
      m += (d-m_value)
      k -= (d-n_value) + (d-m_value)
  print(k)
