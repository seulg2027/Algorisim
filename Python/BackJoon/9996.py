# 9996 한국이 그리울 땐 서버에 접속하지


# 단순하게 봤다가 예외처리 때문에 애를 먹었던 문제
import sys

N = int(sys.stdin.readline().rstrip())

pattern = sys.stdin.readline().rstrip()
pattern_left, pattern_right = pattern.split('*')

for _ in range(N):
  data = sys.stdin.readline().rstrip()
  if data[0:len(pattern_left)] == pattern_left and data[-len(pattern_right):] == pattern_right: # 패턴과 일치할 경우
    if len(pattern_left) + len(pattern_right) <= len(data):
      print("DA")
      continue
  print("NE")