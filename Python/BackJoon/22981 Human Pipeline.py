# 22981 휴먼 파이프라인


# 시간초과ㅠ_ㅠ 엥 억울해
# 목요일에 다시 풀어보기
n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def team_divide():
  global k
  critial = 0 # 팀 나누는 구분선
  work_speed = 0
  while critial < n - 1:
    team_left = data[0:critial+1] # 왼쪽 팀 # 슬라이싱
    team_right = data[critial+1:n] # 오른쪽 팀 # 슬라이싱
    min_left = team_left[0]
    min_right = team_right[0]
    value = min_left * (critial + 1) + min_right * (n - critial - 1)
    
    work_speed = max(value, work_speed) # 더 큰 값 고르기
    critial += 1
  if k % work_speed == 0:
    return k / work_speed # 작업 시간 리턴
  else: # 나머지가 있을 경우
    return k // work_speed + 1

print(int(team_divide()))