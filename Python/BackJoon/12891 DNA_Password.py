# 12891번 DNA 비밀번호

import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input()
num = list(map(int, input().split()))
alpabet = ['A', 'C', 'G', 'T']
st = dict()
for i in range(4):
  st[alpabet[i]] = num[i]

pw = dict({ 'A': 0, 'C': 0, 'G': 0, 'T': 0 })
for i in range(p):
  pw[dna[i]] += 1

def password_check():
  for al in alpabet:
    if pw[al] < st[al]:
      return False # pw 안됨
  return True

cnt = 0
for j in range(p, s):
  if password_check() == True:
    cnt += 1
  pw[dna[j]] += 1
  pw[dna[j-p]] -= 1

if password_check() == True:
  cnt += 1

print(cnt)