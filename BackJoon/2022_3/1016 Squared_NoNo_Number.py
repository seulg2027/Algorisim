# 1016 제곱 ㄴㄴ 수

# 에라토스테네스의 체 사용했는데도 시간초과ㅋ ㅋ ㅋㅋㅋ
# 이 문제는 언제쯤 혼자 풀거야...

import sys, math
input = sys.stdin.readline

m, n = map(int,input().split())
num = [True for _ in range(n - m + 1)]

for i in range(2, int(math.sqrt(n - m + 1))+1):
  j = 1
  while i*i*j < m:
    j += 1
  while i*i*j <= n+1:
    num[i*i*j - m] = False
    j += 1

cnt = 0
for i in range(n-m+1):
  if num[i]:
    cnt += 1
print(cnt)

# 답지@_@

import math
min, max = map(int, input().split())
validate = [1 for i in range(max-min+1)]
cnt=0
i=2
while i**2 <= max:
  mul = min // i**2
  while mul * (i**2) <= max:
    if mul * (i**2) - min >= 0 and mul * (i**2) - min <= max-min:
      validate[mul * (i**2) - min] = 0
    mul +=1
  i +=1

print(sum(validate))