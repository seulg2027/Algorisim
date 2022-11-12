'''
17678 셔틀버스
아이디어가 중요
1. 막차를 타려고 기다리는 사람 수, 마지막 셔틀버스에 마지막으로 타는 사람의 시간 구하기
2. 막차를 타려고 기다리는 사람 수가 m보다 크면 마지막 셔틀버스에 마지막으로 타는 사람의 시간에서 1분 일찍 도착
    m보다 작으면 막차시간에 딱 맞춰서 도착하면 됨
'''

import datetime

def get_time(t, shuttle):
    shuttle_list = shuttle.split(":")
    sh_time = datetime.time(int(shuttle_list[0]), int(shuttle_list[1]))
    delta = datetime.timedelta(minutes=t)
    aft_time = datetime.datetime.combine(datetime.date(1,1,1), sh_time) + delta
    hour = str(aft_time.hour) if len(str(aft_time.hour)) == 2 else "0" + str(aft_time.hour)
    minute = str(aft_time.minute) if len(str(aft_time.minute)) == 2 else "0" + str(aft_time.minute)
    shuttle = hour + ":" + minute
    return shuttle

def solution(n, t, m, timetable):
    answer = ''
    con_list = []
    shuttle = "09:00"
    waiting = [] # 기다리는 순서
    for i in range(n): # 버스 올 때마다
        tt = len(timetable)
        
        if i > 0: # 그 다음 셔틀버스 시간
            shuttle = get_time(t, shuttle)
        for j in range(tt):
            now = timetable.pop(0)
            now_list = now.split(":")
            sh_list = shuttle.split(":")
            now_time = datetime.time(int(now_list[0]), int(now_list[1]))
            sh_time = datetime.time(int(sh_list[0]), int(sh_list[1]))
            if now_time <= sh_time:
                waiting.append(now)
            else:
                timetable.append(now)
        waiting.sort()
        len_wt = len(waiting) # 기다리는 사람
        for z in range(m): # 탈 수 있는 사람만큼 waiting에서 제외
            try:
                wt = waiting.pop(0)
                if i == n-1:
                    if len_wt >= m:
                        if m-1 == z: # 제일 늦게 탄 사람
                            con_list.append(get_time(-1, wt))
            except: break
    
    if con_list == []:
        answer = shuttle
    else:
        answer = con_list[-1]
    
    return answer