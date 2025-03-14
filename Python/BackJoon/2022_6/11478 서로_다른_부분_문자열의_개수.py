# 11478번 서로 다른 부분 문자열의 개수

# 투포인터 떠올림
# 근데 집합 자료구조를 왜... 안떠올림..? 중복 불가한건 집합!

import sys
input = sys.stdin.readline

s = input().rstrip()
s_set = list(set(s))

cnt = 0
result = set()

while cnt < len(s):
  for l in range(len(s)):
    right = l + cnt
    rs = s[l:right+1]
    result.add(rs)
  cnt += 1

print(len(result))