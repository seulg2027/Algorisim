# 2108번 통계학

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
  numbers.append(int(input()))

numbers.sort()
com_numbers = Counter(numbers).most_common(2)

print(round(sum(numbers)/n))
print(numbers[n//2])
if len(com_numbers) > 1:
  if com_numbers[0][1] == com_numbers[1][1]:
    print(com_numbers[1][0])
  else:
    print(com_numbers[0][0])
else:
  print(com_numbers[0][0])
print(numbers[-1] - numbers[0])