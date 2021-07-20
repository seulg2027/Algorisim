# Q10 자물쇠와 열쇠

# 내가 풀려고 시도한 아이디어
# key를 우회전, 좌회전 시켜보고 리스트 비교후 덧셈을 했을 때 모두 1이 되면 true값 반환하기
# 덧셈이 2이상이 나오면 우회전, 좌회전부터 다시 실행하기

# import sys
# input = sys.stdin.readline

# key = list(map(input()))
# lock = list(map(input()))
# N = 0
# M = 0

# for i in key:
#   M += 1

# for j in lock:
#   N += 1

# # def turn_left():
# #   if M % 2 == 0 : # 짝수인 경우


# def turn_right():
#   if M % 2 == 0 : # 짝수인 경우


# 답안 예시
## 자물쇠, 열쇠의 크기 < 20X20
## 그러므로 모든 경우의 수를 계산해볼 수 있음
## 자물쇠의 가로, 세로 크기를 모두 3배로 키운 뒤(왜냐하면 바깥에도 리스트가 더해질 수 있게 하게끔...)

def rotate_a_matrix_by_90_degree(a):
  n = len(a) #행길이 계산
  m = len(a[0]) #열길이 계산
  result = [[0]*m for _ in range(m)] #결과 리스트
  for i in range(n):
    for j in range(m):
      result[j][n - i -1] = a[i][j] # 이거 외우고 있어야겠다...후
  return result

def check(new_lock): # 새로 만든 자물쇠의 중간 부분이 모두 1인지 확인
  lock_length = len(new_lock)//3 # 크기를 세배 했으므로 3을 나눠줌
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1: # 1이 아니면
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  new_lock = [[0] * (n*3) for _ in range(n*3)] # 자물쇠의 크기를 기존의 3배로 전환
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n] = lock[i][j]
  
  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    for x in range(n * 2): # 자물쇠 부분   # n의 3배가 아닌 2배인 이유는 열쇠를 넣으면 또 더해지므로...
      for y in range(n * 2):
        for i in range(m): # 자물쇠에 열쇠 넣기
          for j in range(m):
            new_lock[x+i][y+j] += key[i][j]
        if check(new_lock) == True:
          return True
        for i in range(m): # 자물쇠에서 열쇠 빼기
          for j in range(m):
            new_lock[x+i][y+j] -= key[i][j]
  return False