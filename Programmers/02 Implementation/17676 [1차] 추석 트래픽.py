'''
추석 트래픽

90점... 너모 어려워
'''

import datetime

def solution(lines):
    answer = 0
    logs_detail = [] # 시작시간, 끝 시간으로 이루어진 로그 상세
    
    for l in lines:
        date, times, sec = list(l.split(" "))
        log = datetime.datetime.strptime(date + " " + times, "%Y-%m-%d %H:%M:%S.%f")
        sec = sec[:-1]
        sec = list(sec.split("."))
        if len(sec) > 1:
            micro = "0" * (6-len(sec[1]))
            m1 = datetime.timedelta(seconds=int(sec[0]), microseconds=int(sec[1] + micro))
        else:
            m1 = datetime.timedelta(seconds=int(sec[0]))
        m2 = datetime.timedelta(microseconds=int("001000"))
        start = log - m1 + m2
        logs_detail.append([start, log])
    
    for i in range(len(logs_detail)):
        cnt = 1
        #print(logs_detail[i][1])
        for j in range(i+1, len(logs_detail)):
            ch = logs_detail[j][0] - logs_detail[i][1]
            if ch.days == -1:
                cnt += 1
                #print(logs_detail[j][0], ch.days, ch.seconds, ch.microseconds)
            elif ch.seconds < 1:
                cnt += 1
                #print(logs_detail[j][0], ch.days, ch.seconds, ch.microseconds)
            elif ch.seconds >= 1:
                break
        answer = max(cnt, answer)


'''
다른 사람 코드

time 함수를 만들어서 밀리초 쓰는게 키포인트..
'''

def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    # datetime 모듈을 안씀..
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1