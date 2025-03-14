# 예제 1번 상하좌우 문제

# 문제를 푸는 방안을 잘 모르겠어서
# 답지를 보고 품...
N = int(input())
data = list(map(str, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
plan_list = ['R', 'L', 'D', 'U']

x, y = 1, 1

for data in data:
    for i in range(len(plan_list)):
        if data == plan_list[i]:
            next_x = x + dx[i]
            next_y = y + dy[i]
    if next_x < 1 or next_x > N or next_y < 1 or next_y > N:
        continue  # 다시 반복문 돈다 (예외)
    x = next_x  # 만약 벗어나지 않으면
    y = next_y

print(x, y)


# 예제 2번 시각 문제

N = int(input())

count = 0
for h in range(N + 1):
    for m in range(60):  # 59초까지 이므로
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):  # 왜 or 가 아니고 플러스일까..
                count += 1

print(count)
