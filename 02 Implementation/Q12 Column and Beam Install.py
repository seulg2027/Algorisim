# Q12 기둥과 보 설치

# 내가 푼 방법
# 바닥에 기둥 세우고 보 붙이는 것까지 함...
import numpy as np

n = int(input())
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]


def Column_i(n, column):
    column_data = [[0]*n for i in range(n)]
    for i in range(n):
        column_data[0][i] = 5
    column = np.array(column)
    column_data = np.array(column_data)
    for z in column[0:len(column), 3]:
        is_install = z
    for y,x in column[0:len(column), 0:2]:
        if column_data[x][y] == 5:
            column_data[x][y] += 2
            column_data[x+1][y] += 1
    return column_data

def Beam_i(n, beam, column_data):
    beam_data = [[0]*n for i in range(n)]
    beam= np.array(beam)
    beam_data = np.array(beam_data)
    for z in beam[0:len(beam), 3]:
        is_install = z
    for y,x in beam[0:len(beam), 0:2]:
        if column_data[x][y] == 1 or column_data[x][y+1] == 1:
            beam_data[x][y] += 2
            beam_data[x][y+1] += 1
    print(column_data)
    print(beam_data)


def solution(n, build_frame):
    n += 1
    column = []
    beam = []
    List = np.array(build_frame)
    for i in range(len(List)):
        if build_frame[i][2] == 0:  # 0인 경우 기둥
            column.append(build_frame[i])
        else:
            beam.append(build_frame[i])
    # 기둥 설치
    column_data = Column_i(n, column)
    # 보 설치
    Beam_i(n, beam, column_data)
    # 결과 내기
    answer = [[]]
    return answer


solution(n, build_frame)
