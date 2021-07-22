# Q11 뱀 문제

# 내가 푼 방법
# 시간 초과....
import sys
input = sys.stdin.readline

N = int(input())  # 보드의 크기 NXN
K = int(input())  # 사과의 개수
apple_location = []

for i in range(K):
    apple_location += list(input().split())  # 사과의 위치

L = int(input())
snake_direction = []

for j in range(L):
    snake_direction += list(input().split())  # 뱀의 방향

data = [[0]*N for _ in range(N)]
snake_location = [[0]*N for _ in range(N)]  # 뱀의 위치
snake_location[0][0] = 1


def map_data():
    for i in range(0, K*2, 2):
        nx = int(apple_location[i])  # 해당 사과의 위치
        ny = int(apple_location[i+1])
        data[nx-1][ny-1] = 1
    return data


# 방향 초깃값
snake = 1


def mv_snake(Dir, snake):
    if snake == 5:
        snake = 1
    if Dir == 'D':
        snake += 1
    elif Dir == 'L':
        snake -= 1
    return snake


count = 0
while True:
    map_data()
    for a in range(0, L*2, 2):  # 그 다음 회전할 시간과 위치
        time = int(snake_direction[a])
        Dir = snake_direction[a+1]
        if count < time:  # 아직 회전할 시간이 안됐을 때 이동한다
            newsnake = []  # 먼저 위치 초기화
            newsnake = [(i, j) for i in range(N)
                        for j in range(N) if snake_location[i][j] == 1]
            if int(newsnake[-1][1]) >= N or int(newsnake[-1][0]) >= N:
                break
            if snake == 1:
                for row in range(1):
                    for col in range(int(newsnake[-1][1]), N):  # 뱀이 오른쪽으로 움직인다
                        if data[int(newsnake[-1][0])][col] == 1:  # 사과가 있을 때
                            # 뱀의 위치를 추가해주고 사과 없어진다
                            data[int(newsnake[-1][0])][col] = 0
                            snake_location[int(newsnake[-1][0])][col] = 1
                        else:  # 사과가 없을 때
                            # 뱀의 위치를 옮겨준다.
                            snake_location[int(newsnake[-1][0])][col] = 1
                            snake_location[int(newsnake[-1][0])][col-1] = 1
                        count += 1
                        if count == time:
                            break
                    if count == time:
                        break
            elif snake == 2:
                for row in range(int(newsnake[-1][0]), N):
                    for col in range(1):
                        if data[row][int(newsnake[-1][1])] == 1:
                            data[row][int(newsnake[-1][1])] = 0
                            snake_location[row][int(newsnake[-1][1])] = 1
                        else:
                            snake_location[row + 1][int(newsnake[-1][1])] = 1
                            snake_location[row][int(newsnake[-1][1])] = 1
                        count += 1
                        if count == time:
                            break
                    if count == time:
                        break
            # elif snake == 3:
            #     for row in range(1):
            #         for col in range(int(newsnake[-1][1]), N):  # 뱀이 오른쪽으로 움직인다
            #             if count == time:
            #                 break
            #         if count == time:
            #             break
        elif count == time:  # 회전할 시간
            snake = mv_snake(Dir, snake)
            continue  # 회전해준다
    break

print(snake_location)

print(count)
