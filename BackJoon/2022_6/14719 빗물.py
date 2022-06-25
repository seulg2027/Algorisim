# 14719 빗물

# 처음 푼 방법 -> 양쪽 블록을 선택해서 묶는 방법

# import sys
# input = sys.stdin.readline

# h, w = map(int, input().split())
# blocks = list(map(int, input().split()))

# cnt = 0
# black_block = 0
# rainwater = 0
# height = [blocks[0]]

# for i in range(1, w):
#   if blocks[i] >= height[-1] or height[-1] >= blocks[i] > blocks[w-1]:
#     if len(height) == 2:
#       height.pop(0)
#     height.append(blocks[i])
#     min_value = min(height)
#     rainwater += cnt * min_value - black_block
#     cnt, black_block = 0, 0
#   else:
#     cnt += 1
#     black_block += blocks[i]

# print(rainwater)


# 두번째 방법 -> 왼쪽 블록과 오른쪽 블록 최고 높이 비교하기

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
  height = min(max(blocks[:i]), max(blocks[i+1:]))
  if height - blocks[i] > 0:
    ans += (height - blocks[i])

print(ans)