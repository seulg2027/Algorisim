# Q18. 괄호 변환

# 시간 초과.. 20분 내에 생각할 수 있는게 없었음🥺
# 재귀적으로 한다고 주어졌는데 머릿속에서 꼬여서 무슨 조건부터 따져야하는지 감을 잡기 어려웠음...
# DFS/BFS를 이용해야한다고 생각해서 덱 사용하는걸 고민하다가 시간날림
p = ")("

def solution(p):
  answer = ''
  cnt_left = 0
  cnt_right = 0
  if p == '':
    return answer
  else:
    for i in range(len(p)):
      if p[i] == '(':
        cnt_left += 1
      elif p[i] == ')':
        cnt_right += 1
      if cnt_left == cnt_right and cnt_left != 0 and cnt_right != 0:
        u = p[:cnt_left+cnt_right-1]
        v = p[cnt_left+cnt_right-1:]
        
  answer = ''
  return answer


# 답안 예시

def balanced_index(p): # 균형잡힌 괄호 문자열의 인덱스
  count = 0
  for i in range(len(p)):
    if p[i] == '(':
      count += 1
    else:
      count -= 1 # 아 변수를 두개 만들지 않아도.. 이런 방법이...
    if count == 0 :
      return i

# 올바른 괄호 문자열인가? 이 함수의 원리를 생각 못함
def check_proper(p):
  count = 0 #왼쪽 괄호의 개수
  for i in p:
    if i == '(':
      count += 1
    else:
      if count == 0: # 쌍이 맞지 않는 경우
        return False
      count -= 1
  return True


def solution(p):
  answer = ''
  if p == '':
    return answer
  index = balanced_index(p)
  u = p[:index + 1]
  v = p[index + 1:] # 여기까지! 생각함
  # 올바른 괄호 문자열
  if check_proper(u):
    answer = u + solution(v)
  else: # 올바른 괄호 문자열이 아니라면
    answer = '('
    answer += solution(v)
    answer += ')'
    u = list(u[1:-1])
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')'
      else:
        u[i] = '('
    answer += "".join(u)
  return answer