# 01 진짜 메세지

# 구현, 문자열 #
# 채점50까지 가고 틀림..........
# 테케를 다 넣어봤는데도 알 수 없음
from collections import deque

result = []

for i in range(int(input())):
  q = deque()
  message = input()
  # 주어진 알파벳이 덱에 없을 경우만 알파벳 삽입
  for alphabet in message:
    if alphabet not in q:
      q.append(alphabet)
  while q: # 큐가 다 빌때까지 반복
    word = q.popleft()
    if message.count(word) % 3 == 0:
      result.append(False) # 진짜 메세지가 아닌 경우
      break # 반복문 종료하고 다음 word를 보지 않는다.
    # 마지막 글자
    if not q:
      # result 리스트 해당 테스트 케이스에 false가 들어가있지 않은 경우
      result.append(True)
      break # 이거 안해주면 while문을 다시 돎... why...

# 한번에 출력하기
for i in range(len(result)):
  print("OK" if result[i] else "FAKE")