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


## 답안 예시

# 현재 설치된 구조물 -> 가능한 구조물인지? 확인하는 함수
# 이걸 놓쳐버림...... 허어어 아예 만들 때 이걸 고려해서 만드려고 했는데 만들고 나서 확인하는 거였다니... 우ㅠㅠㅠㅠ
# 그리고 기둥과 보 데이터를 다 만들 필요는 없다 result만 반환해주면 되지!
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥인 경우
            # '바닥 위' or '보 한쪽 끝부분 위' or '다른 기둥 위'
            if y == 0 or [x-1, y-1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: # 보인 경우
            if [x, y-1] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
        return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame # 와 이렇게 한꺼번에 할당할 수 있구나
        if operate == 0: # 삭제하는 함수
            answer.remove([x, y, stuff])
            if not possible(answer): # 직관적으로 코드가 나와서 좋넹
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)