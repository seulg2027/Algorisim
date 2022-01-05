# 잃어버린 괄호

s = input()
for i in range(len(s)):
  if s[i] == '-':
    left, right = s[:i], s[i:]
    break
  left, right = s, ''

if left != '':
  left_num = list(left.split('+'))
else:
  left_num = ''

right_num = right.replace('+', '-').strip()
right_num = list(right_num.split('-'))
result = 0

for plus in left_num:
  if '' == plus:
    continue
  result += int(plus)
for minus in right_num:
  if '' == minus:
    continue
  result -= int(minus)

print(result)