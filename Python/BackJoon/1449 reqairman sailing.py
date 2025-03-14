# 수리공 항승

n, l = map(int, input().split())
sorted_tape = sorted(list(map(int, input().split())))

result = 0
idx = 0
i = 0

while True:
  if idx == n:
    break
  critical = sorted_tape[idx] + (l - 1)
  for tape in sorted_tape[idx:]:
    if critical >= tape:
      i += 1
      if sorted_tape.index(tape) == (n-1):
        result += 1
        idx = n
    else:
      idx = i
      result += 1
      break

print(result)