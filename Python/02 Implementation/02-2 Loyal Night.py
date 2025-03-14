# 2번 왕실의 나이트


# 내가 푼 방법
location = input()
count = 0

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = [1, 2, 3, 4, 5, 6, 7, 8]

index_col = col.index(location[0])
index_row = row.index(int(location[1]))

if index_col - 2 > 0 and index_row - 1 > 0:
    count += 1
elif index_col - 2 > 0 and index_row + 1 < 7:
    count += 1
elif index_col + 2 < 7 and index_row - 1 > 0:
    count += 1
elif index_col + 2 < 7 and index_row + 1 < 7:
    count += 1
if index_row - 2 > 0 and index_col - 1 > 0:
    count += 1
elif index_row - 2 > 0 and index_col + 1 < 7:
    count += 1
elif index_row + 2 < 7 and index_col - 1 > 0:
    count += 1
elif index_row + 2 < 7 and index_col + 1 < 7:
    count += 1

print(count)


# 답안 예시
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
         (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]  # 행에서 이동하는 위치 확인
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
