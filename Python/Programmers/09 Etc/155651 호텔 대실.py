'''
155651번 호텔 대실
누적합으로 구하기
'''

MAX_TIME = 24 * 60 # 모든 분 타임라인
HOUR = 60

def solution(book_time):
    answer = 0
    timeline = [0] * (MAX_TIME + 10) # 10분간 청소를 해야하므로 +10
    
    for t in book_time:
        start_t = list(map(int, t[0].split(":")))
        end_t = list(map(int, t[1].split(":")))
        start_min = start_t[0] * HOUR + start_t[1]
        end_min = end_t[0] * HOUR + end_t[1]
        for i in range(start_min, end_min + 10):
            timeline[i] += 1
    
    answer = max(timeline)
    
    return answer