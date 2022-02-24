# 1759번 암호 만들기

# 백트래킹 사용
# 고려해야할 사항이 많았음.. 자음 두개 이상 이라던지

import sys
input = sys.stdin.readline

l, s = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()
alpha = ['a', 'e', 'i', 'o', 'u']
visited = [0 for _ in range(s)]
st = ''

vo = []
so = []
for i in alphabet: 
  if i in alpha:
    vo.append(i)
  else:
    so.append(i)

def is_print(s):
  cnt1, cnt2 = 0, 0
  for i in range(l):
    if s[i] in so:
      cnt1 += 1
    if s[i] in vo:
      cnt2 += 1
  return True if cnt1 >= 2 and cnt2 >= 1 else False

def make_pw(x, idx):
  global st
  if x == l:
    if is_print(st):
      print(st)
  else:
    for i in range(idx, s):
      if not visited[i] and not alphabet[i] in st:
        al = -1
        if st:
          s_idx = st[-1]
          al = alphabet.index(s_idx)
        if al < i:
          visited[x] = 1
          st += alphabet[i]
          make_pw(x+1, idx+1)
          visited[x] = 0
          st = st[:-1]

make_pw(0, 0)