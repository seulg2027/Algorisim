'''
176962 과제 진행하기

얼레벌레 풀었당..

1) 과제를 시간순으로 배열하기 (오름차순) -> 시간을 모두 분으로 나타내서 계산 난이도 내리기
2) 하나의 과제마다 검사하기
  - 중간에 멈추게 된 과제는 스택으로 쌓기
  - 그 다음 과제를 수행하기까지 시간이 모자라지 않으면 바로 answer에 넣기
    - 시간이 더 남는다면, 스택에서 꺼내서 과제 하기

'''


from collections import deque

def solution(plans):
    answer = []
    stack = deque([])
    plans_sort = sorted(plans, key=lambda x: x[1])
    
    # 시간 -> 분으로 변경하기
    for i in range(len(plans_sort)):
        start = plans_sort[i][1].split(":")
        plans_sort[i][1] = int(start[0])*60 + int(start[1])
    
    # 검사하기
    for j in range(len(plans_sort)-1):
        study = plans_sort[j+1][1]-plans_sort[j][1]
        if study < int(plans_sort[j][2]): # 과제하는 시간이 더 걸릴 때
            stack.append([(plans_sort[j][0], int(plans_sort[j][2])-study)])
        else: # 과제를 마침
            answer.append(plans_sort[j][0])
            remind_t = study-int(plans_sort[j][2])
            while remind_t>0:
                if not stack:
                    break
                now = stack.pop()
                if remind_t < now[0][1]:
                    stack.append([(now[0][0], now[0][1]-remind_t)])
                    remind_t = 0
                else:
                    answer.append(now[0][0])
                    remind_t -= now[0][1]
    
    answer.append(plans_sort[-1][0])
    for x in reversed(stack):
        answer.append(x[0][0])
    
    return answer