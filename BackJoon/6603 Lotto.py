# 6603번 로또

import sys
input = sys.stdin.readline

def make_lotto(x):
  global k
  if x == 7:
    for i in range(1, 7):
      print(lotto[i], end=' ')
    print()
  else:
    for i in range(k):
      if max(lotto) < num[i]:
        lotto[x] = num[i]
        make_lotto(x+1)
        lotto[x] = 0

while True:
  data = list(map(int, input().split()))
  k = data[0]
  if k == 0:
    break
  num = data[1:]
  lotto = [0] * 7
  make_lotto(1)
  print()