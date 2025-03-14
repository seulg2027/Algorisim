# 숫자 문자열과 영단어

s = "2three45sixseven"

list_s = []
for item in s:
  list_s += item

def solution(s):
  table = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
  }
  answer = 0
  cnt = 0 # 숫자 자리수 세어줄 변수
  word = '' # word 덩어리
  while s:
    st = s.pop()
    if 97 <= ord(st) <= 122: # 문자인 경우
      word = st + word
      for i in list(table.keys()):
        if word == i:
          answer += table[word] * (10 ** cnt)
          cnt += 1
          word = ''
          break
    else:
      answer += int(st) * (10 ** cnt)
      cnt += 1
  return answer

print(solution(list_s))