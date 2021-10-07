# 2156 포도주 시식

# 확실히 정확성은 된거같은데.. 메모리 초과 남
# 조합을 사용했으니 당연함ㅠ 다시 풀어봐야 해
# 자꾸 같은 코드가 반복돼서 봤더니 dp문제였다ㅎ
import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip())
data = []
com = list(combinations(range(N), 4))

for i in range(N):
  amount = int(sys.stdin.readline().rstrip())
  data.append((amount, i))

# 마실 수 있는지 판별해주는 함수
def is_drinking(idx):
  cnt_1, cnt_2, cnt_3 = 0, 0, 0
  if (idx - 2 >= 0 and idx < N):
    cnt_1 = sum(drinking[idx-2:idx+1])
  if (idx - 1 >= 0 and idx + 1 < N):
    cnt_2 = sum(drinking[idx-1:idx+2])
  if (idx >= 0 and idx + 2 < N):
    cnt_3 = sum(drinking[idx:idx+3])
  if (cnt_1 < 3 and cnt_2 < 3 and cnt_3 < 3):
    return True
  return False

result = 0
drinking = [0] * N # 마셨는지 안마셨는지 표시해주는 인덱스

for method in com:
  value = 0
  for i in method:
    now, index = data[i]
    drinking[index] = 1
    if is_drinking(index) == True: # 마실 수 있다면
      value += now
    else: # 아니면 반복문 중단
      break
  for i in method:
    now, index = data[i]
    drinking[index] = 0
  result = max(result, value)

print(result)