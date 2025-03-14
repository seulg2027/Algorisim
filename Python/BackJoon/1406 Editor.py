# 에디터

# BFS를 이용해 푼 듯
# 계속 시간초과 나서... 우째야할지 모르겠다..
import sys
from collections import deque

data_left = sys.stdin.readline()
n = int(sys.stdin.readline())

data_right = ''
data_cursor = data_left + data_right
edit_force = []

for _ in range(n):
  edit_force += list(map(str, sys.stdin.readline().split()))

q = deque()
push_list = []

for i in range(len(edit_force)): # 문자열의 길이만큼 반복함
  if edit_force[i] == 'P' or edit_force[i] == 'L' or edit_force[i] == 'B' or edit_force[i] == 'D':
    q.append(edit_force[i]) # 큐에 P, L, B, D 를 차례대로 넣는다.
    if edit_force[i] == 'P':
      push_list.append(edit_force[i+1])

k = 0

while q:
  edit = q.popleft()
  if edit == "P":
    data_left += push_list[k]
    k += 1
  if edit == "L": # 커서 왼쪽으로 옮기기
    if len(data_left) > 0:
      data_right = data_left[-1] + data_right
      if len(data_left) > 1:
        data_left = data_left[:-1]
      elif len(data_left) == 1:
        data_left = ''
  if edit == "B": # 커서 있는 왼쪽 삭제
    data_left = data_left[:-1]
  if edit == "D": # 커서 오른쪽으로 한칸
    if len(data_right) > 0:
      data_left += data_right[0]
      if len(data_right) > 1: # 오른쪽이 2개 이상일 경우만 오른쪽 갱신
        data_right = data_right[1:]
      elif len(data_right) == 1:
        data_right = ''
  data_cursor = data_left + data_right

print(data_cursor)