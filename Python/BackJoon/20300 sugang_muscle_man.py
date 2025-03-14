# 서강 근육맨

n = int(input())
muscle = sorted(list(map(int, input().split())))
m = 0

if n % 2 == 0: # 짝수인 경우
  for i in range(int(n/2)):
    m = max(m, muscle[i]+muscle[n-i-1])
else: # 홀수인 경우
  m = muscle[n-1]
  for j in range(int(n//2)):
    m = max(m, muscle[j]+muscle[n-j-2])

print(m)