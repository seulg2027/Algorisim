# 다리를 지나는 트럭

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
  answer = 0
  completed = []
  bridge = [0] * bridge_length
  size = len(truck_weights)
  while len(completed) < size:
    answer += 1
    now = bridge.pop(0)
    if now != 0: # 0이 아닌 다리라면
      completed.append(now) #완료로 넘겨주기
    if len(truck_weights) > 0: # 아직 다리 건너지 않은 것이 남아있다면
      if sum(bridge) + truck_weights[0] <= weight:
        bridge.append(truck_weights.pop(0))
      else:
        bridge.append(0)
  return answer

print(solution(bridge_length, weight, truck_weights))