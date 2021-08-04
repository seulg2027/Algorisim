# 실패율

# 내가 푼 방법
# 프로그래머스 돌린결과 : 정답률 33.3%
# 테스트 케이스 결과가 이해안감
def key(data):
  return data[1]

def solution(N, stages):
  stages.sort()
  length = len(stages)
  max_stage = stages[length-1]

  total_person = 0
  stage = [] # 각 스테이지의 실패율 담을 리스트 만들기
  result =[] # 결과값 리스트만들기
  for i in range(1, max_stage+1):
    not_clear_person = stages.count(i) # 스테이지에 도달했으나 클리어하지 못한 플레이어의 수
    for j in range(length): # 각 스테이지별로 그 스테이지보다 높거나 같은 스테이지에 있는 플레이어 수 구하기
      if i <= stages[j]:
        total_person += 1 # 그 스테이지에 도달한 플레이어 수
    failure = not_clear_person/total_person # 실패율 계산
    stage.append([i, failure]) # 스테이지랑 실패율 같이 넣기
    total_person = 0
    not_clear_person = 0
  stage = sorted(stage, key=key, reverse=True)
  for stage_failure in stage:
    result.append(stage_failure[0])
  return result

N = 4
stages = [4,4,4,4,4]

print(solution(N, stages))