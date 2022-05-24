# 1543번 문서 검색

# 주어진대로 풀이, 단 반례 주의...

import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()
point = 0
start = 0
cnt = 0

while start < len(doc)-(len(word)-1):
  for j in range(start, len(doc)):
    if doc[j] == word[point]:
      if point == len(word)-1:
        cnt += 1
        point = 0
        start = j+1
        break
      else:
        point += 1
    else:
      point = 0
      start += 1
      break


print(cnt)