# 1181번 단어 정렬

import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
  words.append(input().rstrip())

sorted_words = sorted(words, key=lambda x: (len(x), x))
printed_words =[]

for word in sorted_words:
  if not word in printed_words:
    printed_words.append(word)
    print(word)