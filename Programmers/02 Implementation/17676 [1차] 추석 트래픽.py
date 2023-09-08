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