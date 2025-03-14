# Q30 가사 검색

# 아이디어 생각 하다가 답지 봄..
words = [ "frodo", "front", "frost", "frozen", "frame", "kakao" ]
queries = [ "fro??", "????o", "fr???", "fro???", "pro?" ]

from bisect import bisect_left, bisect_right

# 특정 데이터의 개수를 반환하는 함수
def count_by_value(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장
array = [[] for _ in range(10001)]
# 앞 리스트를 뒤집어서 저장 # 접두사에 와일드 카드가 올 경우 계산할거임
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
  answer = []
  for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

  for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()
  
  for q in queries: # 쿼리를 하나씩 확인하며 처리
    # 이걸 어떻게 생각해요.......
    if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
      res = count_by_value(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
    else: # 접두사에 와일드 카드가 붙은 경우
      res = count_by_value(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
    # 검색된 단어의 개수 저장
    answer.append(res)
  return answer