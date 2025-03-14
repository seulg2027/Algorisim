# 국영수

# 내가 푼 방법
# 백준 - 시간초과
n = int(input())

students = []

for i in range(n):
  students.append(input().split())

def kor_report(students):
  return students[1] 

students = sorted(students, key=kor_report, reverse=True)

for j in range(n):
  for i in range(n-1):
    if students[i][1] == students[i+1][1]: # 국어 점수가 같을 경우
      if students[i][2] > students[i+1][2]: # 영어 점수가 증가하는 순서로 만든다.
        students[i], students[i+1] = students[i+1], students[i]
      elif students[i][2] == students[i+1][2]: # 국어, 영어 점수가 같을 경우
        if students[i][3] > students[i+1][3]: # 수학 점수가 감소하는 순서로 만든다.
          students[i], students[i+1] = students[i+1], students[i]
        elif students[i][3] == students[i+1][3]: # 국영수 점수가 같을 경우
          if ord(students[i][0][0]) > ord(students[i+1][0][0]):
            students[i], students[i+1] = students[i+1], students[i]

for student in students:
  print(student[0])

###################################   답안 예시    ###################################

n = int(input())
students = []

for _ in range(n):
  students.append(input().split())

## 정렬기준 :
## 1 두번째 원소를 기준으로 내림차순 정렬
## 2 두번째 원소 같은 경우, 세번째 원소 기준으로 오름차순 정렬 .... 이것의 반복


students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])) #와.....와......말도안돼ㅠ

for student in students:
  print(student[0])