# 3 게임 개발

# 40분 초과
# 테스트 케이스 예시만 통과... 나머지 예시는 통과 못함ㅠㅠ

# 내가 푼 방법
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

data = [[0]*M for i in range(N)]  # 갔는지 안갔는지 여부를 알려주는 데이터
count = 0  # 간 횟수를 세어준다.

data[x][y] = 1  # 처음 서있는 곳에서 출발
array = []  # 바다인지 육지인지 데이터

for i in range(N):
    array.append(list(map(int, input().split())))


def turn_left():
    global direction
    if direction < 3:
        direction += 1
    else:  # 서쪽인 경우
        direction = 0


# data 변경 / 북, 동, 남, 서
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def move_data(x, y):  # 케이스를 잘못 계산한 듯......
    global direction
    while True:
        current_direction = direction
        if current_direction != direction:
            nx = x + dx[direction]
            ny = y + dy[direction]
            if data[nx][ny] == 0 and array[nx][ny] == 0:
                x, y = nx, ny
                data[x][y] = 1
        else:  # 처음에 바라봤던 방향으로 돌아왔으면 뒤로 간다
            if (direction - 2) >= 0:
                nx = x + dx[direction-2]
                ny = y + dy[direction-2]
            else:
                nx = x + dx[direction+2]
                ny = y + dy[direction+2]
            if array[nx][ny] == 1:
                break  # 뒷면이 바다일 경우 이 반복문을 끝낸다
            x, y = nx, ny  # 뒷면이 육지일 경우 뒤로 가서 다시 방향 잡기
            data[x][y] = 1
        turn_left()


move_data(x, y)

for i in data:
    count += i.count(1)

print(count)


# 답안 예시
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0]*M for i in range(N)]  # 갔는지 안갔는지 여부를 알려주는 데이터

d[x][y] = 1
array = []

for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0  # 그 자리에서 몇번 회전했는지 세어준다.
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 이후 정면에 가보지 않은 칸 존재 + 육지인 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우(뒤로가기)
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:  # 뒤가 바다로 막혀있는 경우
            break
        turn_time = 0

print(count)
