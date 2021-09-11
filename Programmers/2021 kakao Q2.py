# 2

# 채점 16개중 10개 통과
n = 110011
k = 10

import string, math

tmp = string.digits+string.ascii_lowercase
def convert(num, digit): # 진수 변환 함수
  q, r = divmod(num, digit)
  if q == 0:
    return tmp[r]
  else:
    return convert(q, digit) + tmp[r]

def is_prime(num):
  x = int(num)
  if x == 2:
    return True
  for i in range(2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
    return True

def solution(n, k):
  answer = 0
  convert_num = convert(n, k)
  convert_num = convert_num.split('0')
  convert_num = ' '.join(convert_num).split()
  for num in convert_num:
    if is_prime(num):
      answer += 1
    else:
      continue
  print(answer)
  return answer

solution(n, k)