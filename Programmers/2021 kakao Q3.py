# 3


# 채점 16개 중 9개 통과
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

from datetime import datetime

def time_calculation(timeTable): # 걸리는 시간 계산하는 함수
  result = []
  for time in timeTable:
    min_add = 0
    if len(time) % 2 != 0 : # 홀
      n = len(time) // 2 + 1
    else :
      n = len(time) // 2
    for i in range(0, n+1, 2):
      if i >= len(time):
        break
      else:
        now = datetime.strptime(time[i], "%H:%M")
        compare = datetime.strptime(time[i+1] if i+1 < len(time) else "23:59", "%H:%M")
        time_interval = compare - now
        min_interval = time_interval.seconds / 60
        min_add += min_interval
    result.append(int(min_add))
  return result

def solution(fees, records):
  answer = []
  id_list = []
  timeTable = [[] for _ in range(500)]
  for item in records:
    time, number, Bool = item.split()
    if number not in id_list:
      id_list.append(number) # 아이디 리스트를 넣어줌
  id_list.sort()
  for item in records:
    time, number, Bool = item.split()
    timeTable[id_list.index(number)].append(time)
  interval = time_calculation(timeTable)
  remove_set = {0}
  result_time = [i for i in interval if i not in remove_set]
  # 주차 요금 계산하기
  for time in result_time:
    if time <= fees[0]:
      answer.append(fees[1])
    else:
      if (time - fees[0]) % fees[2] == 0: # 나누어지는 경우
        extend_time = (time - fees[0]) // fees[2]
      else:
        extend_time = (time - fees[0]) // fees[2] + 1
      answer.append(fees[1] + extend_time * fees[3])
  return answer

solution(fees, records)